import json
from datetime import datetime

from django.test import TestCase, Client

from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework_jwt.settings import api_settings

from .models import Tweet
from profiles.models import Profile

from model_mommy import mommy


class TweetAPITestCase(TestCase):
    def setUp(self):
        self.user = mommy.make(Profile, username='admin')
        self.user.set_password('admin')
        self.user.save()
        self.tweet = mommy.make(Tweet, content='Hello, Test!')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self.user)
        self.token = jwt_encode_handler(payload)
        self.auth = 'JWT {0}'.format(self.token)
        self.client = Client()

    def test_tweets_create(self):
        data = {
            'content': 'I am learning how to do testings in Django'
        }
        response = self.client.post(
            '/tweets/',
            data=data,
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 201)

    def test_tweets(self):
        response = self.client.get(
            '/tweets/',
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.json()), 1)
        self.assertEquals(response.json()[0]['content'], 'Hello, Test!')

    def test_tweets_detail(self):
        response = self.client.get(
            '/tweets/{}/'.format(self.tweet.id),
            HTTP_AUTHORIZATION=self.auth
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['content'], self.tweet.content)

    # def test_tweets_update(self):
    #     data = {
    #         'id': self.tweet.id,
    #         'content': 'content',
    #     }
    #     content_type = 'application/json'
    #     response = self.client.patch(
    #         '/tweets/{}/'.format(self.tweet.id),
    #         json.dumps(data),
    #         content_type=content_type,
    #         HTTP_AUTHORIZATION=self.auth
    #     )
    #     self.assertEquals(response.status_code, 200)
    #     self.assertEquals(response.json(), data)

    # def test_tweets_delete(self):
    #     response =  self.client.delete(
    #         '/tweets/{}/'.format(self.tweet.id),
    #         HTTP_AUTHORIZATION=self.auth
    #     )
    #     self.assertEquals(response.status_code, 204)
