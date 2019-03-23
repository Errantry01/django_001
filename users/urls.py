"""定义当前子应用下的所有路由"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(路径的正则, 视图函数的名字)
    # url(r'^users/index/$', views.index)

    url(r'^index/$', views.index),
    # 路由的匹配顺序是自上而下

    url(r'^say/$', views.say),
    url(r'^sayhello/$', views.say_hello)

]
