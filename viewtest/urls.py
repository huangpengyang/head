#!/bin/bash/env python
# coding:utf-8
from django.urls import path, re_path,include
from viewtest import views
from login_auth import views as view
from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter()
router.register('books5', views.BookView5)
router.register('books7', views.BookView7)
router.register('books8', views.LoginView)
router.register('publish', views.PublishView)
router.register('users', views.UserLoginView)
print(router.urls)
urlpatterns = [
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>/', views.BookViewSingle.as_view()),
    path('books1/', views.BookView2.as_view()),
    path('books1/<int:pk>/', views.BookViewSingle2.as_view()),
    path('books3/', views.BookView3.as_view()),
    path('books3/<int:pk>/', views.BookViewSingle3.as_view()),
    path('books4/', views.BookView4.as_view()),
    path('books4/<int:pk>/', views.BookViewSingle4.as_view()),
    # path('books5/', views.BookView5.as_view({'get': 'list', 'post': 'create'})),
    # path('books5/<int:pk>/', views.BookView5.as_view({'put': 'update', 'delete': 'destroy','get':'retrieve'})),
    path('books6/', views.BookView6.as_view({'get': 'sun'})),
    # path('',include(router.urls)),
    # path('sendmail',views.BookView7.as_view()),

]
urlpatterns += router.urls
