from django.contrib import admin

# Register your models here.
from .models import Area, User, MountainPass

admin.site.register(Area)
admin.site.register(User)
admin.site.register(MountainPass)

