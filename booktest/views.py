from django.shortcuts import render


# Create your views here.

"""
GET /books/ 提供所有记录
POST /books/ 新增⼀条记录
GET /books/<pk>/ 提供指定id的记录
PUT /books/<pk>/ 修改指定id的记录
DELETE /books/<pk>/ 删除指定id的记录
响应数据 JSON
"""

from django.views import View
from datetime import datetime
from django.http import JsonResponse, HttpResponse
import json


from .models import BookInfo, HeroInfo

class BookListView(View):
    """列表视图"""
    def get(self, request):
        """查询所有图书接口"""

        # 1.查询出所有图书模型
        books = BookInfo.objects.all()
        # 2.遍历查询集，取出每一个书籍模型对象，把模型对象转化成字典
        book_list = []
        for book in books:
            book_dict = {
                'id':book.id,
                'btitle':book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            }
            book_list.append(book_dict)
        # 3.响应
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """新增图书接口"""
        # 1. 获取前段传入的请求数据（ｊｓｏｎ） request.body
        json_ste_bytes = request.body
        # 2.把bytes类型字符串转换成json_str
        json_str = json_ste_bytes.decode()
        # 利用json.loads 讲json字符串转换成json(字典/列表)
        book_dict = json.loads(json_str)

        # 创建模型对象并保存（把字典转成模型并存储）
        book = BookInfo(
            btitle=book_dict['btitle'],
            bpub_date=book_dict['bpub_date']
        )
        book.save()

        # 响应（２０１）
        # 把新增的模型转成字典
        json_book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }
        return JsonResponse(json_book_dict, status=201)




class BookDetailView(View):
    """详情视图"""
    def get(self,request, pk):
        """查询制定某个图书接口"""
        # 1.获取出指定ｐｋ的那个模型对象
        try:
            book = BookInfo.objects.get(id=pk)

        except BookInfo.DoesNotExist:
            return HttpResponse({'massage':'查询的数据不存在'}, status=404)
        # 2.模型对象转字典
        book_dict = {
            'id':book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        # 3. 响应
        return JsonResponse(book_dict)



    def put(self, request, pk):
        """修改指定图书接口"""
        # 先查询要修改的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message':'要修改的数据不存在'}, status=404)

        # 获取前段传入的数据（把数据转换成字典）
        book_dict = json.loads(request.body.decode())

        # 重新给模型指定的属性赋值
        book.btitle = book_dict['btitle']
        book.bpub_date = book_dict['bpub_date']
        # 调用save方法
        book.save()
        #  把修改后的模型转换成字典　　　响应
        json_book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''

        }
        return JsonResponse(json_book_dict)



    def delete(self, request, pk):
        """删除指定图书接口"""
        try:
            book = BookInfo.objects.get(id=pk)

        except BookInfo.DoesNotExist:
            return HttpResponse({'message':'删除数据不存在'}, status=404)

        # book.is_delete = True

        book.delete()

        return HttpResponse(status=204)


