# coding: utf-8
from django.shortcuts import render_to_response, redirect
from models import Video, Category


def video_list(request):
    category_id = int(category_id)
    category = Category.objects.get(id=category_id)
    videos = Video.objects.filter(category=category).order_by("-last_update_timestamp")
    return render_to_response(
        "video/video_list.html",
        {"videos": videos, "c": category,},
    )


def video_detail(request, video_id):
    video=Video.object.get(av_id=video_id)
    return render_to_response(
        "video/video_detail.html",
        {"video": video}
    )


def category_list(request):
    categories = Category.objects.all().order_by("-id")
    return render_to_response(
        "category/category_list.html", {"categories": categories}
    )


def index(request):
    return render_to_response("index.html")