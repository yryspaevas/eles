from django.db import models
from account.models import User

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
