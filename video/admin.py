from django.contrib import admin
from models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "owner",
        "create_timestamp",
        "last_update_timestamp",
    )
    search_fields = ["title", "content", "owner"]
    list_filter = ("category",)

admin.site.register(Video, VideoAdmin)