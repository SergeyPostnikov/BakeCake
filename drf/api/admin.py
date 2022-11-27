from django.contrib import admin
from . import models


class CakeAdmin(admin.ModelAdmin):
    list_display = [
        'pk'
        ]

admin.site.register(models.Cake, CakeAdmin)
admin.site.register(models.User, CakeAdmin)
admin.site.register(models.Order, CakeAdmin)