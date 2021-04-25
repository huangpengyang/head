#!/bin/bash/env python
# coding:utf-8
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('students',views.StudentView.as_view()),
    path('books',views.BookView.as_view()),
    path('books/<int:id>/',views.BookView_One.as_view()),
    path('publishs/',views.PublishView.as_view()),
]