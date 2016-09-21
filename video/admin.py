from django.contrib import admin
from models import Video, Category


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "desc",
        "manager",
        "create_timestamp"
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)