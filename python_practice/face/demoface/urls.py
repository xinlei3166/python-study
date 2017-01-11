from django.conf.urls import url
from demoface import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^\d+/$', views.bbs),
]
