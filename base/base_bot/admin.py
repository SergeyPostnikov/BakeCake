from django.contrib import admin

from . import models

class BotAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cake_level', 'cake_form', 'cake_topping', 'cake_berries', 'cake_dekor', 'cake_inscription', 'cake_comment']
    list_editable = ['cake_level', 'cake_form', 'cake_topping', 'cake_berries', 'cake_dekor', 'cake_inscription', 'cake_comment']

admin.site.register(models.Cake, BotAdmin)
