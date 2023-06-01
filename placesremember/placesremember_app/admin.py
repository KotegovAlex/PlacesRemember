from django.contrib import admin

from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user_id", "photo", "time_create", "lon", "lat")
    list_display_links = ("id", "title")
    search_fields = ("title",)


admin.site.register(Place, PlaceAdmin)
