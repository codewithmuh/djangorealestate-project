from django.contrib import admin

from . import models


@admin.register(models.Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "message"]


