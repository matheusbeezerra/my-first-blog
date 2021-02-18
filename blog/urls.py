from django.urls import path
from . import views

urlpatterns = [
    path(r'ˆ$', views.post_list, name='post_list'),
]