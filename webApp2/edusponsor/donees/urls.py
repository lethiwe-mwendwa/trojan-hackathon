from django.conf.urls import url
from . import views

app_name = 'donees'

urlpatterns = [
    url(r'^$', views.donee_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.donee_detail, name="detail"),
]
