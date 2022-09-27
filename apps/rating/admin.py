from django.contrib import admin

from . import models


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["rater", "agent", "rating"]

