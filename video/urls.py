from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^detail/(?P<video_id>\d+)/$', "video.views.video_detail", name='video_detail'),
    url(r'^list/$', "video.views.video_list", name='video_list'),
    url(r'^category/$', 'video.views.category_list', name='test'),
]
