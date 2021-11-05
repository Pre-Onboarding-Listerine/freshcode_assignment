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
        self.menu2 = {
            "category": "qweasdqeasd",
            "name": "asddas",
            "description": "123qwe",
            "is_sold": "DDD",
            "badge": "NEW"
        }
        self.client = Client()

    def tearDown(self):
        Menu.objects.all().delete()

    def test_register_menu_post_success(self):

        response = self.client.post("/api/menus", json.dumps(self.menu), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['category'], self.menu['category'])
        self.assertEqual(response.data['name'], self.menu['name'])
        self.assertEqual(response.data['description'], self.menu['description'])
        self.assertEqual(response.data['is_sold'], self.menu['is_sold'])
        self.assertEqual(response.data['badge'], self.menu['badge'])

    def test_register_menu_post_fail(self):

        response = self.client.post("/api/menus", json.dumps(self.menu2), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_menu_put_success(self):
        self.client = Client()

        menu = {
                id = 
                category 
                name 
                description
                is_sold
                badge
        }
        response = self.client.put('/api/menus/1')
        self.assertEqual(response.status_code, 201)
    
    def test_update_menu_put_fail(self):
        self.client = Client()

        headers = {'HTTP_Authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.zZ8gW9Xqg2Qy4ilOjv1iQWM-XqpaU-AVgVfz7FkUzfQ'}
  
        menu = {
                id = 
                category =
                name = 
                description =
                is_sold =
                badge =
                }

        response = self.client.put('/api/menus/1', json.dumps(menu), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 201)

    def test_destroy_menu_delete_success(self):
        self.client = Client()
        headers = {'HTTP_Authorization': 'token'}
        response = self.client.delete('/api/menus/1', **headers)

        self.assertEqual(response.status_code, 201)
    
    def test_destroy_menu_delete_fail(self):
        self.client = Client()
        headers = {'HTTP_Authorization': 'token'}
        response = self.client.delete('/api/menus/1', **headers)

        self.assertEqual(response.status_code, 401)
