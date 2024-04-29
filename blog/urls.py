from django.urls import path, include
from .views import CategoryView, PostView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('post', PostView)

urlpatterns = [
    path('', include(router.urls)),
]
