from django.db import models
from django.db.models.signals import post_save

from users.models import User
from hashtags.models import Hashtag


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    thumbnail = models.ImageField(
        upload_to="thumbnails/", blank=True)
    content = models.TextField(blank=False)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def add_hashtags(sender, instance, **kwargs):
    tags = instance.tags
    arr = tags.split(', ')
    for tag in arr:
        if (Hashtag.objects.filter(tag=f"#{tag.lower()}")):
            new_tag = Hashtag.objects.filter(tag=f"#{tag.lower()}")[0]
            instance.hashtags.add(new_tag)
        else:
            new_tag = Hashtag.objects.create(tag=tag.lower())
            instance.hashtags.add(new_tag)


post_save.connect(add_hashtags, sender=Blog)
