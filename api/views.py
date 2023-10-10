from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response

from app.models import CustomUser, Post, Category

from .serializers import CustomUserSerializers, CategorySerializers, PostSerializers
from .permissions import (CustomUserPermission,
CustomUserDetailPermission,
CategoryPermission,
CategoryDetailPermission,
PostPermission,
PostDetailPermission
)

@api_view(['GET', 'POST'])
@permission_classes([CustomUserPermission])
def custom_user(request):
    if request.method == 'GET':
        custom_user = CustomUser.objects.all()
        serializer = CustomUserSerializers(custom_user, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CustomUserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CustomUserDetailPermission])
def custom_user_detail(request, pk):

    customuser = CustomUser.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CustomUserSerializers(customuser)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CustomUserSerializers(CustomUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customuser.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@permission_classes([CategoryPermission])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CategoryDetailPermission])
def category_detail(request, pk):

    category = Category.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializers(category)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@permission_classes([PostPermission])
def post(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializers(post, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([PostDetailPermission])
def post_detail(request, pk):

    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Post.delete()
        return Response(status=HTTP_204_NO_CONTENT)
