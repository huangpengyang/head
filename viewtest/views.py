from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from app01.models import *
from rest_framework.response import Response
from viewtest.serializers import *
from rest_framework.generics import GenericAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, \
    UpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

from rest_framework.request import Request
# 第一层 继承 APIView
class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        ser = BookModelSerializer(instance=book_list, many=True)
        return Response(ser.data, status=status.HTTP_423_LOCKED)
        # return NewResponse(data=ser.data,code=100,info='成功',)

    def post(self, request):
        ser = BookModelSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class BookViewSingle(APIView):
    def get(self, request, pk):
        book_obj = Book.objects.filter(pk=pk).first()
        ser = BookModelSerializer(instance=book_obj)
        return Response(ser.data)

    def put(self, request, pk):
        book_obj = Book.objects.filter(pk=pk).first()
        ser = BookModelSerializer(instance=book_obj, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def delete(self, request, pk):
        row = Book.objects.filter(pk=pk).delete()
        if row[0] > 0:
            return Response('')
        else:
            return Response({'info': '用户输入的信息不存在'})

from rest_framework.renderers import JSONRenderer
# 第二层 继承 GenericAPIView
class BookView2(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    renderer_classes = [JSONRenderer,]

    def get(self, request):
        qs = self.get_queryset()
        ser = self.get_serializer(qs, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class BookViewSingle2(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        ser = self.get_serializer(obj)
        return Response(ser.data)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        ser = self.get_serializer(instance=obj, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        res = self.get_object().delete()
        if res[0] > 0:
            return Response('')
        return Response({'info': '用户删除的信息不存在'})


# 第三层 GenericAPIView+5个视图扩展类
class BookView3(ListAPIView, CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class BookViewSingle3(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# 第四层 9个视图子类 GenericAPIView+5个视图扩展类之一，之二，或之三
class BookView4(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class BookViewSingle4(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# 第五层 视图集
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.viewsets import ViewSet, GenericViewSet, ViewSetMixin


# ModelViewSet 5个接口都有
# ReadOnlyModelViewSet：只有读的两个接口
# ViewSet是：ViewSetMixin, views.APIView
# GenericViewSet是：ViewSetMixin, GenericAPIView
# ViewSetMixin:魔法

### 如果视图类继承了ViewSetMixin这个类，路由写法就需要 path('publish/', views.PublishView.as_view({'get': 'list', 'post': 'create'})),


###如果视图类继承了ViewSetMixin这个类，路由的as_view执行的是ViewSetMixin的as_view
# class PublishView(ModelViewSet):
#     queryset = models.Publish.objects.all()  # 要序列化的数据
#     serializer_class = serializer.PublishSerializer  # 要序列化的类
class BookView5(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


#
# class BookViewSingle5(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer


# class PublishView(GenericViewSet): # 路由变了，其它都没变
#     queryset = models.Publish.objects.all()  # 要序列化的数据
#     serializer_class = PublishSerializer  # 要序列化的类
#     def lqz(self,request):
#         qs = self.get_queryset()  # 推荐用self.get_queryset来获取要序列化的数据
#         ser = self.get_serializer(qs, many=True)  # 推荐使用self.get_serializer获取实例化后并且传入数据的对象
#         return Response(ser.data)
from rest_framework import status
from viewtest.response import NewResponse


class BookView6(GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def sun(self, request):
        qs = self.get_queryset()
        ser = self.get_serializer(qs, many=True)
        return NewResponse(data=ser.data, code=100, info='成功', status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


from rest_framework.decorators import action
from django.core.mail import send_mail
from Drf import settings
from rest_framework.mixins import CreateModelMixin

class BookView7(ViewSetMixin, CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSER

    @action(methods=['post'], detail=False)
    def send_mail(self, request, *args, **kwargs):
        print(222)
        send_user = request.data.get('send_user')
        print(111)
        recv_user = request.data.get('recv_user')
        title = request.data.get('title')
        content = request.data.get('content')
        print(333)
        send_mail(title, content, send_user, [recv_user, ])
        print(44)
        return NewResponse(info='短信发送成功')


class LoginView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    @action(methods=['post'],detail=False)
    def login(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(name=username,password=password).first()
        if user:
            request.session['user_info'] = username
            return NewResponse(code=100,info='用户登录成功')
        return NewResponse(code=101,info='用户不存在')

class AuthLogin():
    def authenticate(self, request):
        print(111)
        print(request.data.get('username'))
        print(request.POST)
        print(request.GET)
        print(request.session.session_key)
        print(request.COOKIES.get('sessionid'))
        if request.session.get('user_info'):
            return None
        raise TypeError('123')



class PublishView(ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSer
    authentication_classes = [AuthLogin,]


class UserLoginView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer