#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
import json

from rest_framework import status
from rest_framework import permissions


import pytest
from mixer.backend.django import mixer

from .base import PostsBaseTest


pytestmark = pytest.mark.django_db


# Create your tests here.
class PostsViewTest(PostsBaseTest):

    def test_send_get_request_via_user_viewset(self):
        # list : GET, POST
        # retrive / patch / destroy / : GET / PUT / DELETE
        url = reverse('user-list')
        data = {
            'username': 'Hello',
            'password': 'World',
            'email': 'inhwan.jung@gmail.com',
            'is_active': True,
        }
        response = self.client.post(url, data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.get(pk=1).username == 'Hello'

        url = reverse('user-detail', args=[1])
        response = self.client.get(url, data=data, format='json')
        # response = self.client.get(url, data=json.dumps(data), content_type='application/json')
        assert response.status_code == status.HTTP_200_OK

        url = reverse('user-detail', args=[1])
        data = {
            'is_active': False,
        }
        response = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == status.HTTP_200_OK

