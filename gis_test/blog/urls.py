from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('get_info/', views.get_info, name='get_info'),
]