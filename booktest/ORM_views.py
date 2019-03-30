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

from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views import View
import json

from booktest.models import BookInfo, HeroInfo
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer


class BookListView(View):

    def get(self,request):
        """查询所有图书"""
        books = BookInfo.objects.all()
        book_dict_list = []
        for book in books:
            book_dict = {
                'id':book.id,
                'btitle':book.btitle,
                'bpub_date':book.bpub_date,
                'bread':book.bread,
                'bcomment':book.bcomment,
                'image':book.image.url if book.image else ''
            }
            book_dict_list.append(book_dict)

        return JsonResponse(book_dict_list, safe=False)


    def post(self, request):
        """增加图书"""
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            bpub_date=datetime.strptime(book_dict.get('bpub_date'), '%Y-%m-%d').date(),

        )

        # 构造响应数据
        response_book_dict = {
            'id':book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(response_book_dict, status=201)



class BookDetailView(View):

    def get(self, request, pk):
        """查询指定图书"""
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        book_dict = {
            'id':book.id,
            'btitle':book.btitle,
            'bpub_date':book.bpub_date,
            'bread':book.bread,
            'bcomment':book.bcomment,
            'image':book.image.url if book.image else ''
        }

        return JsonResponse(book_dict)



    def put(self, request, pk):
        """修改指定图书"""
        try:
            book = BookInfo.objects.get(id=pk)

        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 读取客户端传入的数据
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        book.btitle = book_dict.get('btitle')
        book.bpub_date = datetime.strptime(book_dict.get('bpub_date'), '%Y-%m-%d').date()
        book.save()

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })

    def delete(self,request, pk):
        """删除指定图书"""
        try:
            book = BookInfo.objects.get(id=pk)

        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)



class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()  # 指明该视图集在查询数据时使用的查询集
    serializer_class = BookInfoSerializer  # 指定序列化器


from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from booktest.models import BookInfo, HeroInfo

# book = BookInfo.objects.get(id=1)
# s = BookInfoSerializer(instance=book)
# s.data

# books = BookInfo.objects.all()
# s = BookInfoSerializer(instance=books, many=True)
# s.data

# hero = HeroInfo.objects.get(id=2)
# s = HeroInfoSerializer(instance=hero)
# s.data

# book = BookInfo.objects.get(id=2)
# s = BookInfoSerializer(instance=book)
# s.data


# data = {
#     'bpub_date': 123
# }
# s = BookInfoSerializer(data=data)
# s.is_valid()
# s.errors

# data = {
#     'btitle':'金瓶梅',
#     'bpub_date':'1999-11-11'
# }
#
# s = BookInfoSerializer(data=data)
# s.is_valid()
# s.validated_data

# data = {
#     'btitle':'大话西游'
# }
# s = BookInfoSerializer(data=data)
# s.is_valid(raise_exception=True)


# data = {
#     'btitle':'速学python',
#     'bpub_date':'1898-10-10'
# }
# s = BookInfoSerializer(data=data)
# s.is_valid()
# s.errors

# data = {'btitle': 'about python', 'bpub_date': '1998-12-1', 'bread': 30, 'bcomment': 20}
# s = BookInfoSerializer(data=data)
# s.is_valid(raise_exception=True)  # False


# data = {'btitle': 'about django', 'bpub_date': '1998-12-1', 'bread': 30, 'bcomment': 20}
# s = BookInfoSerializer(data=data)
# s.is_valid(raise_exception=True)
# book = s.save()
# book

# book = BookInfo.objects.get(id=6)
# data = {'btitle': 'python_django', 'bpub_date': '1998-12-1', 'bread': 30, 'bcomment': 20}
# s = BookInfoSerializer(book, data=data)
# s.is_valid(raise_exception=True)
# s.save()
#
# book = BookInfo.objects.get(id=6)
# data = {'btitle': '学习django'}
# s = BookInfoSerializer(instance=book, data=data, partial=True)
# s.is_valid(raise_exception=True)
# s.save()
#
# serializer = BookInfoSerializer()
# serializer








