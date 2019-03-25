from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator


# Create your views here.

"""
类视图必须继承View
类视图中的方法都必须是请求方法名小写
"""
def my_decorator(func):
    """定义装饰器视图"""
    def wrapper(request, *args, **kwargs):
        print("装饰器被调用了")
        print(request.method)

        return func(request, *args, **kwargs)

    return wrapper



@method_decorator(my_decorator, name='dispatch')
class DemoView(View):
    """定义类视图"""

    def get(self, request):
        """GET请求业务逻辑"""
        return HttpResponse('get请求')

    def post(self,request):
        """POST请求业务逻辑"""
        return HttpResponse('post请求')



class TemplatesView(View):
    """渲染模板演示"""
    def get(self, request):
        context = {
            'city': '深圳',
            'alist': [1,2,3],
            'adict': {'name': 'zhangsan'}

        }

        return render(request,'index.html', context)





