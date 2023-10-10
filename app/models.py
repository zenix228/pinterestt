from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    bio = models.TextField()
    image = models.ImageField(upload_to='customuser-images')

    def __str__(self):
        return f'{self.username}'

class Category(models.Model):
    name = models.CharField(max_length=251)
    slug = models.SlugField(max_length=250, unique=True)
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категорию'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):                           
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=260, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post-images')

    def __str__(self):                           
        return f'{self.title}'
