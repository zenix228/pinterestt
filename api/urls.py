from django.contrib import admin
from django.urls import path, include
from .views import custom_user, custom_user_detail, category, category_detail, post, post_detail

urlpatterns = [
    path('users/', custom_user),
    path('users/<int:pk>/', custom_user_detail),
    path('category/', category),
    path('category/<int:pk>', category_detail),
    path('posts/', post),
    path('posts/<int:pk>/', post_detail),

    path('auth', include('dj_rest_auth.urls'))
]