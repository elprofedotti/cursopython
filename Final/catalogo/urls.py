from django.urls import re_path as url
from django  import urls
from . import views

urlpatterns =[
      url(r'^$', views.index, name='index'),
      url(r'^listaPeliculas/$', views.listaPeliculas.as_view(), name='listaPeliculas'),
      url(r'^listaDirectores/$', views.listaDirectores.as_view(), name='listaDirectores'),
      #path(r'listaPeliculas/<pk>', views.peliculaDetalle.as_view(), name='peliculaDetalle')
      url(r'^listaPeliculas/(?P<pk>\d+)$', views.peliculaDetalle.as_view(), name='peliculaDetalle'),
      url(r'^listaDirectores/(?P<pk>\d+)$', views.directorDetalle.as_view(), name='directorDetalle'),
]
