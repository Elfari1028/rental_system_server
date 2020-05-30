from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['u_name', 'u_id', 'u_tel',
                     'u_email', 'u_age', 'u_type', 'u_sex', 'c_time']
    list_display = ['u_name', 'u_id', 'u_tel',
                    'u_email', 'u_age', 'u_type', 'u_sex']
