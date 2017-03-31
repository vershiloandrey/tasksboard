from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^task_list$', views.task_list, name='task_list'),
    url(r'^task_detail/(?P<task_id>\d+)/$', views.task_detail),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^$', views.login, name='page_login'),
]
