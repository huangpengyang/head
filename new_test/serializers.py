#!/bin/bash/env python
# coding:utf-8
from rest_framework import serializers
from app01.models import *
from rest_framework.exceptions import ValidationError


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 3
        # extra_kwargs = {
        #     'publish': {'required': True, 'write_only': True},
        #     'authors': {'required': True, 'write_only': True},
        # }
    price_info = serializers.IntegerField(source='price')
    publish= serializers.CharField(source='publish.email')
    publish_email= serializers.CharField(source='publish.email')

    # publish_info = serializers.SerializerMethodField(read_only=True, source='publish')
    # def get_publish_info(self, obj):
    #     res = {'nid': obj.publish.nid, 'name': obj.publish.name, 'price': obj.publish.city, 'date': obj.publish.email}
    #     return res
    #
    # author_info = serializers.SerializerMethodField(source='authors', read_only=True)
    #
    # def get_author_info(self, obj):
    #     res = [{'nid': author.nid, 'name': author.name, 'age': author.age, 'author_detail': author.author_detail_id} for
    #            author in obj.authors.all()]
    #     return res


class PublishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'
        extra_kwargs = {'name': {'max_length': 10, 'error_messages': {'max_length': '最大超度不超过10'}}}


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        extra_kwargs = {
            'age': {'max_value': 150, 'min_value': 1,
                    'error_messages': {'max_value': '最大不超过150岁', 'min_value': '最小1岁'}},
            'author_detail': {'write_only':True},
        }
    author_info = serializers.SerializerMethodField( source='author_detail',read_only=True)
    def get_author_info(self,obj):
            res = {'nid':obj.author_detail.nid,'telephone':obj.author_detail.telephone}
            return res
    def validated_name(self, data):
        if len(data) > 6:
            raise ValidationError('你输入字符已经超过6位')
        else:
            return data



class AuthDetModelSer(serializers.ModelSerializer):
    class Meta:
        model = AuthorDatail
        fields = '__all__'

    def create(self, validated_data):
        res = AuthorDatail.objects.create(**validated_data)
        return res