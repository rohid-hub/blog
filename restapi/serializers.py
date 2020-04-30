from rest_framework import serializers
from users.models import User
from blogs.models import Blog
from hashtags.models import Hashtag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'username', 'email', 'full_name', 'profile_picture')


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'author', 'hashtags', 'tags', 'title',
                  'thumbnail', 'content', 'published_date', 'last_updated')
