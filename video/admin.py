from django.contrib import admin
from models import Video, Category, Author, VideoCategory


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "content",
        "url",
        "av_id",
        "create_timestamp",
        "last_update_timestamp",
    )
    list_filter = ("author",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "desc",
        "create_timestamp"
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author_url",
    )


class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "video_id",
        "category_id",
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(VideoCategory, VideoCategoryAdmin)