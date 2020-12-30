from django.db import models
from django.contrib.auth.models import User
from stats.models import Article

class Comment(models.Model):
    content = models.TextField(max_length=512)
    publish = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)