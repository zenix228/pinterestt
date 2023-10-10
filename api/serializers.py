from rest_framework import serializers
from app.models import CustomUser, Category, Post

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'password',
            'bio',
            'image',
        ]

        def get_image(self, obj):
            request = self.context.get('request')
            if obj.image:
                image = obj.image.url
                return request.build_absolute_uri(image)
            return None
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'