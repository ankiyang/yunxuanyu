# coding: utf-8
from django.shortcuts import render_to_response, redirect
from models import Video, Category


def category_video_list(request):
    return render_to_response(
        "video/video_list.html",
    )


def video_detail(request):
    return render_to_response(
        "video/video_detail.html",
    )


def index(request):
    return render_to_response("index.html")


def all_video(request):
    return render_to_response("video/all_video.html")