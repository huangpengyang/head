#!/bin/bash/env python
# coding:utf-8
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    # views得到的对象，通过序列化器进行需要字段的转换
    name = serializers.CharField()
    age = serializers.IntegerField()

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)

    price = serializers.IntegerField()
    publish_id = serializers.IntegerField(source='publish.nid')
    authors_info = serializers.CharField(source='authors.name',max_length=32)
    publish = serializers.SerializerMethodField()
    def get_publish(self,obj):
        res = {'id':obj.publish.nid,'name':obj.publish.name,'city':obj.publish.city}
        return res

    authors = serializers.SerializerMethodField()
    def get_authors(self,obj):
        res = [{'id':x.nid,'name':x.name,'age':x.age} for x in obj.authors.all()]
        return res

class PublishSerializer(serializers.Serializer):
    nid = serializers.IntegerField()
    name = serializers.CharField(max_length=32)
    city_info = serializers.CharField(max_length=32,source='city')

