#!/bin/bash/env python
# coding:utf-8
from rest_framework.response import Response
class NewResponse(Response):
    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None,code=100,info=None,**kwargs):
        dic = {'statuses':code,'info':info}
        if data:
            dic['data'] = data
        if kwargs:
            dic.update(kwargs)

        super().__init__(data=dic,status=status,
                 template_name=template_name, headers=headers,
                 exception=exception, content_type=content_type)
