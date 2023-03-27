from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    marked = models.BooleanField()

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.title