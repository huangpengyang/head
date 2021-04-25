from django.shortcuts import render, HttpResponse

from rest_framework.viewsets import ModelViewSet
from app01.models import *
from app01.serializers import StudentModelSerializer


# Create your views here.
def index(request):
    return HttpResponse('OK')


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


