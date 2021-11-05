# import json
# import unittest
#
# from django.test import Client
# from rest_framework import status
#
# from menus.models import Item, Menu
#
#
# class ItemTest(unittest.TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#         self.menu1 = {
#             "category": "SALAD",
#             "name": "깔라마리 달래 샐러드",
#             "description": "해산물 샐러드",
#             "is_sold": False,
#             "badge": "NEW"
#         }
#         Menu.objects.create(**self.menu1)
#
#         self.item1 = {
#             "name": "미디움",
#             "size": "M",
#             "price": 8000,
#             "is_sold": False
#         }
#         self.item2 = {
#             "name": "라지",
#             "size": "L",
#             "price": 10000,
#             "is_sold": "asd"
#         }
#
#     def tearDown(self) -> None:
#         Item.objects.all().delete()
#
#     def test_create_item_with_correct_data(self):
#         response = self.client.post(
#             "/api/menus/1/items",
#             data=json.dumps(self.item1),
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['menu_id'], self.item1['menu_id'])
#         self.assertEqual(response.data['name'], self.item1['name'])
#         self.assertEqual(response.data['size'], self.item1['size'])
#         self.assertEqual(response.data['price'], self.item1['price'])
#         self.assertEqual(response.data['is_sold'], self.item1['is_sold'])
#
#     def test_create_item_with_incorrect_data(self):
#         response = self.client.post(
#             "/api/menus/1/items",
#             data=json.dumps(self.item2),
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
