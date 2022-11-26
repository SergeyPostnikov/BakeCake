from django.contrib import admin
from . import models


class CakeAdmin(admin.ModelAdmin):
    list_display = [
        'pk'
        ]

admin.site.register(models.Cake, CakeAdmin)