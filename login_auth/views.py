from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ViewSetMixin,ModelViewSet
from app01.models import *
from login_auth.serializers import *
# Create your views here.
class UserLoginView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer