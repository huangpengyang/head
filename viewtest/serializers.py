#!/bin/bash/env python
# coding:utf-8
from rest_framework import serializers
from app01.models import *
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'price':{'required':False},
            'publish_date':{'required':False},
            'publish':{'required':False},
            'authors':{'required':False},
            # 'authors':{'allow_blank':True,'allow_null':True},
        }

class EmailSER(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class PublishSer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'


from rest_framework.exceptions import ValidationError
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password':{'min_length':3,'max_length':16,'error_messages':{'min_length':'密码最少3位','max_length':'密码最多16位'}}
        }
    def validated_name(self,data):
        if data.startswith('sb'):
            raise ValidationError('名字不能以sb开头')
        return data