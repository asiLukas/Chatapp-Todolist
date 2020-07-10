from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_30_messages(self):
        return Message.objects.order_by('-created').all()[:30]
