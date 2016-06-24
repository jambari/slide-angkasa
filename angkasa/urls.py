from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^angkasa/$', views.angkasa_view, name = 'angkasa_view'),
    url(r'^angkasasatu/$', views.angkasasatu_view, name = 'angkasa_satu'),
    url(r'^angkasadua/$', views.angkasadua_view, name = 'angkasa_dua'),
]
