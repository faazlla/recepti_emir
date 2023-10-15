from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return(f"{self.name} {self.image}")
    