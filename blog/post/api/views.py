from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView


from post.api.serializers import PostSerializer
from post.models import Post
#default permissions
from rest_framework.permissions import (IsAuthenticated, IsAdminUser)
#custom permissions
from post.api.permissions import IsOwner


# Create your views here.

class PostListAPIView(ListAPIView):

    serializer_class = PostSerializer
    #search işlemi yapılır. field ile hangi columnların içinde geçtiğine bakarak search yapar. bu işlemler searchfilter ile yapılır.
    #OrderingFilter ile hangi column'a göre orderby işlemi yapılır. url kısmında sorgunun sonuna ? konur ve search= veya ordering= kullanılarak işlemler gerçekleştirilir. ordering işleminde ordering=- kullanımı ile tersden sıralama işlemi yapılır.
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','content']
    #sorguları filtreleme işlemi
    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

#UpdateAPIView kullanırsak güncelleme işlemi sırasında içleri boş gelir. ama RetrieveUpdate kullanırsak mevcut değerler görünür.
class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner, IsAdminUser]

    # override update,create methodları yerine perform_update,create kullanabiliriz.
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

