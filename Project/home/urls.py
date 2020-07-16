from django.urls import path, re_path, include
from . import views

urlpatterns = [
	re_path(r'^$', views.home),
	re_path(r'^next/', include('next.urls')),
]