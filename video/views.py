# coding: utf-8
from django.shortcuts import render_to_response, redirect
from models import Video, Category, VideoCategory


def category_list(request):
    categories = Category.Objects.all().order_by("-id")
    return render_to_response(
        "category_list.html",
        {"categories": categories}
    )


def category_video_list(request, category_id):
    category_id = int(category_id)
    category = Category.objects.get(id=category_id)
    videos = VideoCategory.objects.get(category=category)
    return render_to_response(
        "video/video_list.html",
        {"videos": videos, "c": category},
    )


def video_detail(request, video_id):
    video_id = int(video_id)
    video = Video.objects.get(id=video_id)
    return render_to_response(
        "video/video_detail.html",
        {"video": video},
    )

def index(request):
    return render_to_response("index.html")


def all_video(request):
    videos = Video.Objects.all().order_by("-id")
    return render_to_response(
        "video/all_video.html",
        {"videos: videos"},
    )

