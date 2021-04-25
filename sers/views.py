from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views import View
from .serializers import StudentSerializer,BookSerializer,PublishSerializer
from app01.models import *
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView


class StudentView(APIView):
    def get(self, request):
        # 实例化序列化器创建序列化器对象
        # 参数
        # instance  模型对象或者模型列表
        # data  进行反序列化阶段使用的数据，数据来自于客户端的提交
        # context 当需要从视图中转发数据到序列化器的时候，可以使用
        # many  当instance参数为模型列表，则many=True
        student_list = Student.objects.all()
        serializer = StudentSerializer(student_list, many=True)
        print(serializer.data)  # data 可以接受所有post的请求数据
        return Response(serializer.data)


class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        print(book_list)
        serializer = BookSerializer(instance=book_list,many=True)
        print(serializer.data)
        return  Response(serializer.data)


class BookView_One(APIView):
    def get(self,request,id):
        book_obj = Book.objects.filter(pk=id).first()
        serializer = BookSerializer(instance=book_obj)
        return Response(serializer.data)


class PublishView(APIView):
    def get(self,request):
        publish_list = Publish.objects.all()
        serializer = PublishSerializer(instance=publish_list,many=True)
        return Response(serializer.data)

from rest_framework.throttling import BaseThrottle
