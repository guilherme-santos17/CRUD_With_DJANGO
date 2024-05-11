from django.db import models

# Create your models here.

class appTask(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title