import json

from django.shortcuts import reverse
from django.test import TestCase, Client

from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from rest_framework_jwt.settings import api_settings

from .models import Profile

from model_mommy import mommy


class ProfileAPITestCase(TestCase):
    def setUp(self):
        self.user = mommy.make(Profile, username='admin')
        self.user.set_password('admin')
        self.user.save()
        self.users = mommy.make(Profile, _quantity=10)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self.user)
        self.token = jwt_encode_handler(payload)
        self.auth = 'JWT {0}'.format(self.token)
        self.client = Client()

    def test_profiles_create(self):
        data = {
            'username': 'goodrink',
            'password': 'goodrink2018',
            'bio': 'startup top de Natal!'
        }
        response = self.client.post(
            '/profiles/',
            data=data,
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 201)

    def test_profiles(self):
        response = self.client.get(
            '/profiles/',
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.json()), 11)
        self.assertEquals(
            response.json()[0]['username'],
            self.user.username
        )

    def test_profiles_detail(self):
        response = self.client.get(
            '/profiles/{}/'.format(self.user.id),
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['username'], self.user.username)

    def test_profiles_update(self):
        data = {
            'username': 'zecolmeia',
            'bio': 'urso esfomeado'
        }
        content_type = 'application/json'
        response = self.client.patch(
            '/profiles/{}/'.format(self.user.id),
            json.dumps(data),
            content_type=content_type,
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), data)

    def test_profiles_delete(self):
        response =  self.client.delete(
            '/profiles/{}/'.format(self.user.id),
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 204)
