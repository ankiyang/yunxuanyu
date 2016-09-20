# coding: utf-8
from django.shortcuts import render_to_response, redirect

from category.models import Category
from models import Video


def video_list(request, category_id):
    category_id = int(category_id)
    category = Category.objects.get(id=category_id)
    videos = Video.objects.filter(category=category).order_by("-last_update_timestamp")
    return render_to_response(
        "video_list.html",
        {"videos": videos, "c": category, },
    )


def video_detail(request, video_id):
    video_id = int(video_id)
    video=Video.object.get(id=video_id)
    return render_to_response(
        "video_detail.html",
        {"video": video}
    )
