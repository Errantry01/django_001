from django.conf.urls import url
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())

    # APIView
    # url(r'^books/$', views.BookListAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailAPIView.as_view()),

    # # Generic
    # url(r'^books/$', views.BookListGenericAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailGenericView.as_view())

    # ViewSet视图集指定路由
    # url(r'^books/$', views.BookViewSet.as_view({'get':'list', 'post':'create'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    #
    #
    # #　增加的行为路由
    # url(r'^books/latest/$', views.BookViewSet.as_view({'get':'latest'})),
    # url(r'^books/(?P<pk>\d+)/read/$', views.BookViewSet.as_view({'put': 'read'})),
]

router = SimpleRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookViewSet)  # 向路由器中注册视图
urlpatterns += router.urls   # 将路由器中的所以路由信息追到到django的路由列表中