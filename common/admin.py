from django.contrib import admin

# Register your models here.

from .models import Users, House, RentalOrder, SupportRequest, SupportRequestConversation, SupportRequestRating, \
    PictureGroup

admin.site.register(Users)
admin.site.register(House)
admin.site.register(SupportRequestRating)
admin.site.register(SupportRequest)
admin.site.register(SupportRequestConversation)
admin.site.register(PictureGroup)
admin.site.register(RentalOrder)
