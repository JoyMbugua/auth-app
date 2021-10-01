from django.contrib import admin
from .models import CustomUser, MagicLink

class CustomUserAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MagicLink)
