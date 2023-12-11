from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "user",
            'title',
            'content',
            "slug",
            "created",
            "image",
            "modified_by"
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

# Post modelimde bazı propertyler editable=false olduğu için create ve update işlemlerinde görünmüyor.
# Bu yüzden tıpkı farklı bir dto gibi farklı bir serializer oluşturup editable alanlarını kapatarak. istediğim şeylerin görünmesini sağlayabiliriz. APIView'lerdeki serializer_class'ları güncellemeyi unutma
# class PostUpdateCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = [
#             'title',
#             'content',
#             "slug",
#             "created",
#             "image"
#         ]