from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Tag(models.Model):
    tag = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish_date = models.DateTimeField('publish date')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)








