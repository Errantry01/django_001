from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from rest_framework.decorators import action

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer



# class BookListAPIView(APIView):
#     def get(self, request):
#         books = BookInfo.objects.all()
#         # 序列化
#         serializer = BookInfoSerializer(books, many=True)
#         return Response(serializer.data)  # 响应序列化结果
#
#     def post(self, request):
#         data = request.data
#         serializer = BookInfoSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class BookDetailAPIView(APIView):
#     """详情视图"""
#     def get(self, request, pk):
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = BookInfoSerializer(instance=book)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = BookInfoSerializer(instance=book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self,request,pk):
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



"""以下是继承GenericAPIView的视图"""
# class BookListGenericAPIView(GenericAPIView):
#
#     # 指定序列化器类
#     serializer_class = BookInfoSerializer
#     # 指定查询集　‘数据来源’
#     queryset = BookInfo.objects.all()
#
#     def get(self, request):
#         qs = self.get_queryset()
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         data = request.data
#         serializer = self.get_serializer(data = data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
# class BookDetailGenericView(GenericAPIView):
#
#     serializer_class = BookInfoSerializer
#     queryset = BookInfo.objects.all()
#
#     def get(self, request, pk):
#         book = self.get_object()
#         serializer = self.get_serializer(book)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         book = self.get_object()
#         serializer = self.get_serializer(book, request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
#     def delete(self, request, pk):
#         book = self.get_object()
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



""" 以下是GenericAPIView和mixin的混合使用视图"""
# class BookListGenericAPIView(CreateModelMixin, ListModelMixin, GenericAPIView):
#
#     # 指定序列化器类
#     serializer_class = BookInfoSerializer
#     # 指定查询集　‘数据来源’
#     queryset = BookInfo.objects.all()
#
#     def get(self, request):
#
#         return self.list(request)
#
#     def post(self, request):
#
#         return self.create(request)
#
#
# class BookDetailGenericView(DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
#
#     serializer_class = BookInfoSerializer
#     queryset = BookInfo.objects.all()
#
#     def get(self, request, pk):
#
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#
#         return self.update(request, pk)
#
#
#     def delete(self, request, pk):
#
#         return self.destroy(request, pk)




"""以下是GenericAPIView和Mixin合成的子类视图"""
# class BookListGenericAPIView(CreateAPIView, ListAPIView):
#
#     # 指定序列化器类
#     serializer_class = BookInfoSerializer
#     # 指定查询集　‘数据来源’
#     queryset = BookInfo.objects.all()
#
#
#
# class BookDetailGenericView(RetrieveUpdateDestroyAPIView):
#
#     serializer_class = BookInfoSerializer
#     queryset = BookInfo.objects.all()



"""以下是APIView的视图集"""
# class BookViewSet(ViewSet):
#     def list(self, request):
#         qs = BookInfo.objects.all()
#         s = BookInfoSerializer(qs, many=True)
#         return Response(s.data)
#
#     def create(self, request):
#         data = request.data
#         s = BookInfoSerializer(data = data)
#         s.is_valid(raise_exception=True)
#         s.save()
#         return Response(s.data)
#
#     def retrieve(self, request, pk):
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         s = BookInfoSerializer(instance=book)
#         return Response(s.data)



"""以下是GenericAPIView的视图集"""
# class BookViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
class BookViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    @action(methods=['get'], detail=False)
    def latest(self, request):
        """查询最后一本书"""
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        """修改图书阅读量"""
        book = self.get_object()
        book.bread = request.data.get('bread')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)








