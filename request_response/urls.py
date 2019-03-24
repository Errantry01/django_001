from django.conf.urls import url

from . import views


urlpatterns = [
    # url(r'^weather/beijing/2018/$', views.weather),

    # url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),

    url(r'^get_query_params/$', views.get_query_params),
    url(r'^get_form_data/$', views.get_form_data),
    url(r'^get_json/$', views.get_json),
    url(r'^get_user/$', views.get_user),
    url(r'^response_demo/$', views.response_demo),
    url(r'^json_response_demo/$', views.json_response_demo, name='json_response_demo'), # name:给路由起别名
    url(r'^redirect_demo/$', views.redirect_demo),

]