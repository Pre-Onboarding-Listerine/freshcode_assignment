import json
import unittest
from unittest import TestCase

from django.test import Client
from rest_framework import status

from items.models import Item
from menus.models import Menu
from tags.models import Tag


class MenuTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        self.menu1 = {
            "category": "SALAD",
            "name": "깔라마리 달래 샐러드",
            "description": "해산물 샐러드",
            "is_sold": False,
            "badge": "NEW",
        }
        self.menu2 = {
            "category": "SALAD",
            "name": "깔라마리 달래 샐러드",
            "description": "해산물 샐러드",
            "is_sold": "asdf",
            "badge": "NEW",
        }
        self.menu3 = {
            "category": "SALAD",
            "name": "졸려졸려 달래 샐러드",
            "description": "해산물 샐러드",
            "is_sold": False,
            "badge": "TIRED",
        }

        self.item1 = {
            "name": "미디움",
            "size": "M",
            "price": 8000,
            "is_sold": False
        }
        self.item2 = {
            "name": "라지",
            "size": "L",
            "price": 10000,
            "is_sold": False
        }

        self.tag1 = {
            "name": "페스코베지테리언",
            "type": "vegetarianism"
        }

    def tearDown(self):
        Menu.objects.all().delete()

    def test_register_menu_post_success(self):
        response = self.client.post("/api/menus", json.dumps(self.menu1), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['category'], self.menu1['category'])
        self.assertEqual(response.data['name'], self.menu1['name'])
        self.assertEqual(response.data['description'], self.menu1['description'])
        self.assertEqual(response.data['is_sold'], self.menu1['is_sold'])
        self.assertEqual(response.data['badge'], self.menu1['badge'])

    def test_register_menu_post_fail(self):
        response = self.client.post("/api/menus", json.dumps(self.menu2), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_menu_delete_success(self):
        menu = Menu.objects.create(**self.menu1)
        headers = {'HTTP_Authorization': 'token'}
        response = self.client.delete("/api/menus/" + str(menu.id), **headers)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_menu_with_correct_data(self):
        menu = Menu.objects.create(**self.menu1)
        changes = {
            "category": "GAMZA",
            "name": "졸려졸려 달래 샐러드",
            "description": "해산물 샐러드",
            "is_sold": False,
            "badge": "NEW",
        }
        response = self.client.put(
            "/api/menus/" + str(menu.id),
            data=json.dumps(changes),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], changes['category'])
        self.assertEqual(response.data['name'], changes['name'])
        self.assertEqual(response.data['description'], changes['description'])
        self.assertEqual(response.data['is_sold'], changes['is_sold'])
        self.assertEqual(response.data['badge'], changes['badge'])

    def test_update_menu_with_incorrect_data(self):
        menu = Menu.objects.create(**self.menu1)
        changes = {
            "category": "GAMZA",
            "name": "졸려졸려 달래 샐러드",
            "description": "해산물 샐러드",
            "is_sold": None,
            "badge": "NEW",
        }
        response = self.client.put(
            "/api/menus/" + str(menu.id),
            data=json.dumps(changes),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_menu_with_partial_data(self):
        menu = Menu.objects.create(**self.menu1)
        changes = {
            "category": "GAMZA",
            "name": "졸려졸려 달래 샐러드",
            "badge": "NEW",
        }
        response = self.client.put(
            "/api/menus/" + str(menu.id),
            data=json.dumps(changes),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_menu_with_partial_data(self):
        menu = Menu.objects.create(**self.menu1)
        changes = {
            "category": "GAMZA",
            "name": "졸려졸려 달래 샐러드",
            "badge": "NEW",
        }
        response = self.client.patch(
            "/api/menus/" + str(menu.id),
            data=json.dumps(changes),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], changes['category'])
        self.assertEqual(response.data['name'], changes['name'])
        self.assertEqual(response.data['badge'], changes['badge'])

    def test_get_menu_detail_with_exist_id(self):
        menu = Menu.objects.create(**self.menu1)
        response = self.client.get("/api/menus/" + str(menu.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], menu.id)

    def test_get_menu_detail_with_item(self):
        menu = Menu.objects.create(**self.menu1)
        self.item1['menu_id'] = menu

        item = Item.objects.create(**self.item1)

        response = self.client.get("/api/menus/" + str(menu.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['items'][0]['id'], item.id)

    def test_get_menu_detail_with_tag(self):
        menu = Menu.objects.create(**self.menu1)
        self.item1['menu_id'] = menu
        self.tag1['menu_id'] = menu

        item = Item.objects.create(**self.item1)
        tag = Tag.objects.create(**self.tag1)

        response = self.client.get("/api/menus/" + str(menu.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['items'][0]['id'], item.id)
        self.assertEqual(response.data['tags'][0]['id'], tag.id)

    def test_get_menus_with_items_and_tags(self):
        menu01 = Menu.objects.create(**self.menu1)
        self.item1['menu_id'] = menu01
        self.tag1['menu_id'] = menu01

        Item.objects.create(**self.item1)
        Tag.objects.create(**self.tag1)

        menu03 = Menu.objects.create(**self.menu3)
        self.item2['menu_id'] = menu03

        Item.objects.create(**self.item2)

        response = self.client.get("/api/menus")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)




