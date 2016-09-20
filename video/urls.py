from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^detail/(?P<video_id>\d+)/$', "video.views.video_detail", name='video_detail'),
    url(r'^list/(?P<category_id>\d+)', "video.views.video_list", name='video_list'),
]
