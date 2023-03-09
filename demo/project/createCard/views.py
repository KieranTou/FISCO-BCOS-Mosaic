# from django.shortcuts import render

# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse

# 视图函数


def createCard_set(request):  # request为网页发送的请求
    return HttpResponse("Hello World!")
