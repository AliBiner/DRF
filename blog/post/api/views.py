from rest_framework.generics import ListAPIView

from post.api.serializers import PostSerializer
from post.models import Post


# Create your views here.

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer