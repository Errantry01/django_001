from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^demoview/$', views.DemoView.as_view()),
    url(r'^templateview/$', views.TemplatesView.as_view()),
    # url(r'^demoview/$', views.my_decorator(views.DemoView.as_view())),
]