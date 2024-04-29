from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    
    permission_classes = [IsAdminOrReadOnly]

    
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    # filterset_fields = ['category'] # id ile işlem yapabiliyoruz
    filterset_fields = ['category__name']
    search_fields = ['title', 'content']
    # ordering_fields = ['category__name']
    ordering_fields = ['title']
    
    permission_classes = [IsAuthenticatedOrReadOnly]
