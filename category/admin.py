from django.contrib import admin
from models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "desc",
        "manager",
        "create_timestamp"
    )

admin.site.register(Category, CategoryAdmin)