
from django.views.generic import ListView
from .models import Post

from django.http import JsonResponse


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 12

    # def render_to_response(self, context, **response_kwargs):
    #     posts = list(self.model.objects.values('lat', 'long'))  # 작업 필터를 적용하고 목록으로 변환
    #     return JsonResponse({'positions': posts}, safe=False)

def get_info(request):
    posts = Post.objects.all().values('farm_num', 'farm_name', 'lat', 'long', 'distance', 'result')
    return JsonResponse(list(posts), safe=False)
