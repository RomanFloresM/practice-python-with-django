from django.contrib import admin

from .models import peliculas, directores

# Register your models here.

admin.site.register(peliculas)
admin.site.register(directores)
