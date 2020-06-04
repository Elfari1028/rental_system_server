from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.PictureGroup)
class PictureGroupAdmin(admin.ModelAdmin):
    search_fields = ['pg_1', 'pg_2', 'pg_3',
                     'pg_4', 'pg_5', 'pg_6', 'pg_7', 'pg_8', 'pg_9']
    list_display = ['pg_1', 'pg_2', 'pg_3',
                    'pg_4', 'pg_5', 'pg_6', 'pg_7', 'pg_8', 'pg_9']
