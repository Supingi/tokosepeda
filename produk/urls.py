from django.conf.urls import url
from . import views

app_name = 'produk'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<nilai>[\s\w\s]+)/$', views.kategori, name='kategori'),
	url(r'^(?P<nilai>[\s\w\s]+)/(?P<sub_nilai>[0-9]+)/$', views.sub_kategori, name='sub_kategori'),
]