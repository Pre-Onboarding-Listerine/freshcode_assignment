import json
import unittest

from assertpy import assert_that
from django.test import Client
from rest_framework import status

from menus.models import Menu


class TestMenus(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()

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

        self.menu1 = {
            "category": "SALAD",
            "name": "깔라마리 달래 샐러드",
            "description": "해산물 샐러드",
            "is_sold": False,
            "badge": "NEW",
            "items": [

            ],
            "tags": [
                self.tag1
            ]
        }

    # def tearDown(self) -> None:
    #     Menu.objects.all().delete()

    def test_create_menu(self):
        response = self.client.post(
            "/api/menus",
            data=json.dumps(self.menu1),
            content_type="application/json"
        )
        assert_that(response.status_code).is_equal_to(status.HTTP_201_CREATED)

        get_res = self.client.get(
            "/api/menus"
        )
        print(get_res)

        update_response = self.client.put(
            "/api/menus/69",
            data=json.dumps(self.menu1),
            content_type="application/json"
        )

        print(update_response)


