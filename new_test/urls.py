#!/bin/bash/env python
# coding:utf-8
from django.urls import path, re_path
from new_test import views

urlpatterns = [
    path('books/', views.BookView.as_view()),
    path('books/<int:id>', views.BookViewSingle.as_view()),
    path('publish/', views.PublishView.as_view()),
    path('publish/<int:id>/', views.PublishViewSingle.as_view()),
    path('authors/', views.AuthorsView.as_view()),
]
