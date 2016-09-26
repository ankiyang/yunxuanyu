from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^detail/(?P<video_id>\d+)/$', "video.views.video_detail", name='video_detail'),
    url(r'^category/(?P<category_id>\d+)/', "video.views.category_video_list", name='category_video_list'),
    url(r'^all/$', 'video.views.all_video', name='all_video'),
]
