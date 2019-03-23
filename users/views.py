from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
路由的定义三种写法:
1. 总 + 子
2. 总
3. 子
"""

def index(request):
    """
    视图函数, 至少要有一个参数
    :param request: 接受请求对象 类型HttpRequest
    :return: 响应对象 HttpResponse
    """

    return HttpResponse("hello world")

def say(request):
    return  HttpResponse("say")

def say_hello(request):
    return HttpResponse("say hello")
