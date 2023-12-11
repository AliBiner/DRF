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

    #validation işlemleri burada yapılır.
    def validate(self, attrs):
        if attrs["title"] == "oguzhan":
            raise serializers.ValidationError("Olmaz")
        return attrs



    #perform_create veya perform_update yerine override methodları kullanabiliriz.
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.slug = validated_data.get("slug", instance.slug)
    #     instance.modified_by = validated_data.get("modified_by", instance)
    #     instance.save()
    #     return instance
    #
    # def create(self, validated_data):
    #     return Post.objects.create(user=self.context['request'].user, **validated_data)

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