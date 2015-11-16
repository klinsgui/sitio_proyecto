from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar_citas),
    url (r'^cita/(?P<pk>[0-9]+)/$', views.detalle_cita),
]
