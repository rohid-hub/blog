from django.db import models
from django.db.models.signals import pre_save


class Hashtag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


def lowercase(sender, instance,  **kwargs):
    tag = instance.tag
    if " " in tag:
        split_value = instance.tag.split(' ')
        tag = split_value[0]
        for t in split_value[1:]:
            if t != "" and ",":
                tag += f"_{t}"
    instance.tag = f"#{tag.lower()}"


pre_save.connect(lowercase, sender=Hashtag)
