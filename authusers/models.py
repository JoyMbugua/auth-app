from django.db import models
from urllib.parse import urlencode, urljoin
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

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
    

    def save(self, *args, **kwargs):
        params = {'code': self.code}
        params['email'] = self.email
        query = urlencode(params)
        
        self.link = query
        return super().save(*args, **kwargs)

    def generate_url(self, request):
        url_path = reverse('dashboardview')

        query = self.link
        url_path = f'{url_path}?{query}'
        domain = get_current_site(request).domain
        scheme = request.is_secure() and 'https' or 'http'
        url = urljoin(f'{scheme}://{domain}', url_path)
        return url
