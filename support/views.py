from django.shortcuts import render

# Create your views here.


@admin.register(models.SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    search_fields = ['sr_id', 'sr_status', 'sr_type', 'sr_content',
                     'sr_time', 'u_id', 'pg_id', 'res_u_id', 'fix_u_id']

    list_display = ['sr_id', 'sr_status', 'sr_type', 'sr_content',
                    'sr_time', 'u_id', 'pg_id', 'res_u_id', 'fix_u_id']


@admin.register(models.SupportRequestConversation)
class RentalOrderAdmin(admin.ModelAdmin):
    search_fields = ['src_id', 'src_content',
                     'src_time', 'sr_id', 'u_id', 'pg_id']

    list_display = ['src_id', 'src_content',
                    'src_time', 'sr_id', 'u_id', 'pg_id']


@admin.register(models.SupportRequestRating)
class RentalOrderAdmin(admin.ModelAdmin):
    search_fields = ['srr_id', 'srr_content',
                     'sr_id', 'srr_stars']

    list_display = ['srr_id', 'srr_content',
                    'sr_id', 'srr_stars']
