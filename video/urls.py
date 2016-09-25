from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^detail/$', "video.views.video_detail", name='video_detail'),
    url(r'^category/$', "video.views.category_video_list", name='category_video_list'),
    url(r'^all/$', 'video.views.all_video', name='test'),
]
