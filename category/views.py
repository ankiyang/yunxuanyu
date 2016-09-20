from django.shortcuts import render_to_response
from models import Category


def category_list(request):
    categories = Category.objects.all().order_by("-id")
    return render_to_response(
        "category_list.html", {"categories": categories}
    )