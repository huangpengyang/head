#!/bin/bash/env python
# coding:utf-8
from rest_framework import serializers
from app01.models import *
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
