from django.contrib import admin

from . import models

class BotAdmin(admin.ModelAdmin):
    list_display = ['pk']

admin.site.register(models.Cake, BotAdmin)
admin.site.register(models.Сake_buyer, BotAdmin)