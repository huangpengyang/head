from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from app01.models import *
from new_test.serializers import BookModelSerializer, PublishModelSerializer,AuthorModelSerializer,AuthDetModelSer
from rest_framework.response import Response
from rest_framework import status

class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        ser = BookModelSerializer(instance=book_list, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = BookModelSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)


class BookViewSingle(APIView):
    def get(self, request, id):
        book_obj = Book.objects.filter(pk=id).first()
        ser = BookModelSerializer(instance=book_obj)
        return Response(ser.data)

    def put(self, request, id):
        book_obj = Book.objects.filter(pk=id).first()
        ser = BookModelSerializer(instance=book_obj, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)

    def delete(self, request, id):
        res = Book.objects.filter(pk=id).delete()
        if res[0] > 0:
            return Response({'info': '数据删除成功'})
        else:
            return Response({'info': '用户输入的用户数据不存在'})


class PublishView(APIView):
    def get(self, request):
        publish_list = Publish.objects.all()
        ser = PublishModelSerializer(instance=publish_list, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = PublishModelSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)


class PublishViewSingle(APIView):
    def get(self, request, id):
        publish_obj = Publish.objects.filter(pk=id).first()
        ser = PublishModelSerializer(instance=publish_obj)
        return Response(ser.data)

    def put(self, request, id):
        publish_obj = Publish.objects.filter(pk=id).first()
        ser = PublishModelSerializer(instance=publish_obj, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)

    def delete(self, request, id):
        res = Publish.objects.filter(pk=id).delete()
        if res[0] > 0:
            return Response({'info': '数据删除成功'})
        else:
            return Response({'info': '用户输入的用户数据不存在'})


class AuthorsView(APIView):
    def get(self, request):
        author_list = Author.objects.all()
        ser = AuthorModelSerializer(instance=author_list, many=True)
        return Response(ser.data)

    def post(self, request):
        author_detail =request.data.pop('author_detail')  # 第一步  取出 author_detail的数据
        ser_res = AuthDetModelSer(data=author_detail)  # 先创建author_detail的数据
        if ser_res.is_valid():
            ser_res.save()  # 触发 AuthDetModelSer下的create的执行
            nid = ser_res.data.get('nid')  # 取出author_detail的nid
            request.data['author_detail']=nid  # 再赋值给data
        ser = AuthorModelSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            instance = ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
