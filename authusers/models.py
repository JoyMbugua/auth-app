from django.db import models
from urllib.parse import urlencode, urljoin
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14, blank=True, null='')
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0)
    code = models.CharField(max_length=10, null='')


class MagicLink(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    redirect_url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    link = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email}==={self.link}"
