import json
import unittest
from unittest import TestCase

from django.test import Client

from menus.models import Menu


class MenuTest(TestCase):

    def setUp(self) -> None:
        self.menu = {
            "category": "qweasdqeasd",
            "name": "asddasfsfafds",
            "description": "123qwe",
            "is_sold": True,
            "badge": "NEW"
        }
        self.client = Client()

    def tearDown(self):
        Menu.objects.all().delete()

    def test_register_menu_post_success(self):

        response = self.client.post("/api/menus", json.dumps(self.menu), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['category'], self.menu['category'])
        self.assertEqual(response.data['name'], self.menu['name'])
        self.assertEqual(response.data['description'], self.menu['description'])
        self.assertEqual(response.data['is_sold'], self.menu['is_sold'])
        self.assertEqual(response.data['badge'], self.menu['badge'])




# class MenuTest(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_register_menu_with_normal_data(self):
#         data = {
#             "category": "qweasdqeasd",
#             "name": "asddasfsfafds",
#             "description": "123qwe",
#             "is_sold": True,
#             "badge": "NEW"
#         }
#         response = self.client.post("/api/menus", data=data, content_type='application/json')
#
#         from pprint import pprint
#         pprint(response.data)
#
#         res = self.client.get("/api/menus")
#         from pprint import pprint
#         pprint(res.data)
