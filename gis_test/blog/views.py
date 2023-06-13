from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 12

def get_info(request):
    posts = Post.objects.all().values('farm_name', 'lat', 'long', 'distance', 'result')
    return JsonResponse(list(posts), safe=False)
