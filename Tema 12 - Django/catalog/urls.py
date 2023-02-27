from django.urls import re_path as url
from django  import urls
from . import views

urlpatterns =[
     #url(r'^$', views.index,name='index', )
     url(r'^$', views.index,name='index', )
]
