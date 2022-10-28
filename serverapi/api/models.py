from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Serverapi(models.Model):
    slack_username = models.CharField(max_length=120)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self) -> str:
        return self.slack_username