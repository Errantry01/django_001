from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())

]

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图
urlpatterns += router.urls   # 将路由器中的所以路由信息追到到django的路由列表中