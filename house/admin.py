from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    search_fields = ['h_id', 'h_name', 'h_status', 'h_term',
                     'h_cap', 'h_intro', 'h_price', 'h_location', 'pg_id']

    list_display = ['h_id', 'h_name', 'h_status', 'h_term',
                    'h_cap', 'h_intro', 'h_price', 'h_location', 'pg_id']


@admin.register(models.RentalOrder)
class RentalOrderAdmin(admin.ModelAdmin):
    search_fields = ['ro_id', 'ro_status', 'ro_type', 'ro_amount',
                     'ro_time', 'ro_start', 'ro_end', 'u_id', 'h_id', 'res_u_id']

    list_display = ['ro_id', 'ro_status', 'ro_type', 'ro_amount',
                    'ro_time', 'ro_start', 'ro_end', 'u_id', 'h_id', 'res_u_id']
