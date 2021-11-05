import json
import unittest

from django.test import Client
from rest_framework import status

from items.models import Item
from menus.models import Menu


class ItemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.menu1 = {
            "category": "SALAD",
            "name": "깔라마리 달래 샐러드",
            "description": "해산물 샐러드",
            "is_sold": False,
            "badge": "NEW",
        }

        self.menu_instance = Menu.objects.create(**self.menu1)

        self.item1 = {
            "menu_id": self.menu_instance.id,
            "name": "미디움",
            "size": "M",
            "price": 8000,
            "is_sold": False
        }
        self.item2 = {
            "menu_id": 1,
            "name": "라지",
            "size": "L",
            "price": 10000,
            "is_sold": False
        }

    def tearDown(self) -> None:
        Menu.objects.all().delete()
        Item.objects.all().delete()

    def test_create_item_with_correct_data(self):
        response = self.client.post(
            "/api/items",
            data=json.dumps(self.item1),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.item1['name'])
        self.assertEqual(response.data['size'], self.item1['size'])
        self.assertEqual(response.data['price'], self.item1['price'])
        self.assertEqual(response.data['is_sold'], self.item1['is_sold'])

    def test_create_item_with_incorrect_data(self):
        response = self.client.post(
            "/api/items",
            data=json.dumps(self.item2),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_update_item_with_correct_data(self):
        item_data = self.item1.copy()
        item_data['menu_id'] = self.menu_instance
        item = Item.objects.create(**item_data)
        changes = {
            "menu_id": self.menu_instance.id,
            "name": "라지",
            "size": "L",
            "price": 8000,
            "is_sold": False
        }
        response = self.client.put(
            "/api/items/" + str(item.id),
            data=json.dumps(changes),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], changes['name'])
        self.assertEqual(response.data['size'], changes['size'])
        self.assertEqual(response.data['price'], changes['price'])
        self.assertEqual(response.data['is_sold'], changes['is_sold'])

    def test_update_item_with_non_fulled_data(self):
        item_data = self.item1.copy()
        item_data['menu_id'] = self.menu_instance
        item = Item.objects.create(**item_data)
        changes = {
            "menu_id": self.menu_instance.id,
            "name": "라지",
            "is_sold": False
        }
        response = self.client.put(
            "/api/items/" + str(item.id),
            data=json.dumps(changes),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_with_non_fulled_data(self):
        item_data = self.item1.copy()
        item_data['menu_id'] = self.menu_instance
        item = Item.objects.create(**item_data)
        changes = {
            "menu_id": self.menu_instance.id,
            "name": "라지",
            "is_sold": False
        }
        response = self.client.patch(
            "/api/items/" + str(item.id),
            data=json.dumps(changes),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], changes['name'])
        self.assertEqual(response.data['is_sold'], changes['is_sold'])

    def test_delete_item_with_exist_item(self):
        item_data = self.item1.copy()
        item_data['menu_id'] = self.menu_instance
        item = Item.objects.create(**item_data)

        response = self.client.delete(
            "/api/items/" + str(item.id)
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_item_with_non_exist_item(self):
        response = self.client.delete(
            "/api/items/1"
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
