from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
# /weather/beijing/2018
def weather(request, year, city):
    """演示获取url路径数据"""
    print(city)
    print(year)
    return HttpResponse("beijing")


def get_query_params(request):
    """演示获取url查询字符串数据"""

    query_dict = request.GET
    # a = query_dict.get("a")
    # print(a)

    # query_dict.get() 获取单个值
    # quety_dict.getlist() 获取某个键的多个值
    return HttpResponse("get_query_params")


def get_form_data(request):
    """演示获取请求体表单数据"""
    query_dict = request.POST
    print(query_dict.get('a'))
    print(query_dict.getlist('like'))
    return HttpResponse("get_form_data")


def get_json(request):
    """演示获取请求体中的非表单数据:json"""
    json_bytes = request.body
    json_str = json_bytes.decode()
    dict = json.loads(json_str) # 将json字符串转换成json字典或列表
    # json.dumps() # 把字典或列表转换成json字符串
    print(dict)
    return HttpResponse('get_json')

def get_user(request):
    """演示获取当前请求对象"""
    print(request.user)
    return HttpResponse('get_user')


def response_demo(request):
    """演示响应对象"""
    return HttpResponse(content="hello")

