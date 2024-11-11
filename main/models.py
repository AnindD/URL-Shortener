from django.db import models
from django.contrib.auth.models import User 


class Shortened_URL(models.Model):
    URL_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="URL_user_main", null=True)
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100)

    def __str__(self):
        return self.short_url






