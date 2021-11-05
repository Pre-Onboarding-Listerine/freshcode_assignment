import json
import unittest

from django.test import Client
from rest_framework import status

from menus.models import Menu
from tags.models import Tag


class TagTest(unittest.TestCase):
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

        self.tag1 = {
            "name": "페스코베지테리언",
            "type": "vegetarianism"
        }

        self.invalid_tag = {
            "name": "페스코베지테리언",
            "type": None
        }

    def test_create_tag_with_valid_data(self):
        tag_data = self.tag1.copy()
        tag_data['menu_id'] = self.menu_instance.id
        response = self.client.post(
            "/api/tags",
            data=json.dumps(tag_data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], self.tag1["name"])
        self.assertEqual(response.data["type"], self.tag1["type"])

    def test_create_tag_with_invalid_data(self):
        invalid_tag_data = self.invalid_tag.copy()
        invalid_tag_data['menu_id'] = self.menu_instance.id
        response = self.client.post(
            "/api/tags",
            data=json.dumps(invalid_tag_data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_tag_with_valid_changes(self):
        tag_data = self.tag1.copy()
        tag_data['menu_id'] = self.menu_instance
        tag = Tag.objects.create(**tag_data)

        valid_changes = {
            "menu_id": self.menu_instance.id,
            "name": "슬리피베지테리언",
            "type": "enjoytired"
        }
        response = self.client.put(
            "/api/tags/" + str(tag.id),
            data=json.dumps(valid_changes),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], valid_changes["name"])
        self.assertEqual(response.data["type"], valid_changes["type"])

    def test_update_tag_with_short_data(self):
        tag_data = self.tag1.copy()
        tag_data['menu_id'] = self.menu_instance
        tag = Tag.objects.create(**tag_data)

        valid_changes = {
            "menu_id": self.menu_instance.id,
            "type": "enjoytired"
        }
        response = self.client.put(
            "/api/tags/" + str(tag.id),
            data=json.dumps(valid_changes),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_tag_with_partial_data(self):
        tag_data = self.tag1.copy()
        tag_data['menu_id'] = self.menu_instance
        tag = Tag.objects.create(**tag_data)

        valid_changes = {
            "menu_id": self.menu_instance.id,
            "type": "enjoytired"
        }
        response = self.client.patch(
            "/api/tags/" + str(tag.id),
            data=json.dumps(valid_changes),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["type"], valid_changes["type"])

    def test_delete_tag_with_exist_id(self):
        tag_data = self.tag1.copy()
        tag_data['menu_id'] = self.menu_instance
        tag = Tag.objects.create(**tag_data)

        response = self.client.delete("/api/tags/" + str(tag.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_tag_with_non_exist_id(self):
        response = self.client.delete("/api/tags/1")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
