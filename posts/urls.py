from django.conf.urls import url, include
from django.contrib.auth.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from posts.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]