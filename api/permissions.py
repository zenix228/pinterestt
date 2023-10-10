from rest_framework.permissions import BasePermission

class CustomUserPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class CustomUserDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
        
class PostPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_authenticated

class PostDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated
        
class CategoryPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_authenticated

class CategoryDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated
        
