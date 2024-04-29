from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )

class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField() # default Read only, create için kullanılamıyor,

    category_id = serializers.IntegerField(write_only=True) # create için id lazım, ayrıca write only ile sadece create ederken göster bu field ı, listelerken gösterme!


    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'category_id',
            'category',
            'is_published',
            'created_date',
        )
