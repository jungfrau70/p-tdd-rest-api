#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class PostsBaseTest(TestCase):
    def test_create_user_model(self):
        User.objects.create(
            username="Jung In Hwan"
        )
        assert User.objects.count() == 1, "Should be equal"
