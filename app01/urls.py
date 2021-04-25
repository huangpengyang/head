#!/bin/bash/env python
# coding:utf-8
from django.urls import path
from app01 import views
from rest_framework.routers import DefaultRouter

urlpatterns = []
router = DefaultRouter()
router.register('students', views.StudentViewSet)
urlpatterns += router.urls
