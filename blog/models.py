from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField()


    def __str__(self) -> str:
        return self.title
    