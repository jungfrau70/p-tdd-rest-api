#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from mixer.backend.django import mixer

from .base import PostsBaseTest


# Create your tests here.
class PostsModelTest(PostsBaseTest):

    def test_create_user_model(self):
        User.objects.create(
            username="Jung In Hwan"
        )
        # import ipdb
        # ipdb.set_trace()
        assert User.objects.count() >= 1, "Should be equal"

    def test_create_superuser_bia_mixer(self):
        # for cnt in range(50):
        super_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
            # import ipdb;
            # ipdb.set_trace()
        assert User.objects.count() == 1, "Should be equal"
        assert super_user.is_superuser == True, "Should be superuser"

    def test_create_user_bia_mixer(self):
        for cnt in range(50):
            user = mixer.blend('auth.User', is_staff=True, is_superuser=False)
            # import ipdb;
            # ipdb.set_trace()
            assert user.is_superuser == False, "Should not be superuser"
        assert User.objects.count() == 50, "Should be equal"
