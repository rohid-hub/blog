from rest_framework import viewsets, permissions
from .serializers import HashtagSerializer, BlogSerializer, UserSerializer
from users.models import User
from hashtags.models import Hashtag
from blogs.models import Blog


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = UserSerializer


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HashtagSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlogSerializer
