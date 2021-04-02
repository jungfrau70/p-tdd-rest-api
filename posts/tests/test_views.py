#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from .base import PostsBaseTest


# Create your tests here.
class PostsViewsTest(PostsBaseTest):
    def test_create_user_model(self):
        User.objects.create(
            username="Jung In Hwan"
        )

        import ipdb
        ipdb.set_trace()
        assert User.objects.count() == 1, "Should be equal"
