from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('', views.max1, name='dgjdd'),
]