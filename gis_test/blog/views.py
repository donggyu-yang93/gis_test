from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.core import serializers
from django.http import JsonResponse


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 12

    def render_to_response(self, context, **response_kwargs):
        posts = list(self.model.objects.values('lat', 'long'))  # 작업 필터를 적용하고 목록으로 변환
        return JsonResponse({'positions': posts}, safe=False)  # safe=False를 사용하여 비사전 객체도 JSON으로 전달