import json
import unittest

from django.test import Client
from rest_framework import status

from members.models import User


class MemberTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def tearDown(self) -> None:
        User.objects.all().delete()

    # def test_login(self):
    #     signup_response = self.client.post(
    #         "/api/members/signup/",
    #         data=json.dumps({
    #             "email": "hello@email.com",
    #             "password": "123qwe"
    #         }),
    #         content_type="application/json"
    #     )
    #
    #     self.assertEqual(signup_response.status_code, status.HTTP_201_CREATED)
    #
    #     signin_response = self.client.post(
    #         "/api/members/signin/",
    #         data=json.dumps({
    #             "email": "hello@email.com",
    #             "password": "123qwe"
    #         }),
    #         content_type="application/json"
    #     )
    #
    #     self.assertEqual(signin_response.status_code, status.HTTP_200_OK)
