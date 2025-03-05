from django.urls import path, re_path
from . import views

urlpatterns = [
    path('api/openai/', views.openai_proxy, name='openai_proxy'),
    re_path(r'^api/openai/(?P<path>.*)$', views.openai_proxy, name='openai_proxy_with_path'),
]
