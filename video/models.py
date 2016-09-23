# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(u"作者名", max_length=100)
    author_url = models.CharField(u"作者主页", max_length=100)


class Category(models.Model):
    name = models.CharField(u"名字", max_length=30)
    desc = models.CharField(u"描述", max_length=150)

    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"


class Video(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(u"标题", max_length=100)
    content = models.CharField(u"视频简介", max_length=100000)
    url = models.CharField(max_length=10000)
    av_id = models.CharField(max_length=100)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = u"视频"


class VideoCategory(models.Model):
    video_id = models.ForeignKey(Video)
    category_id = models.ForeignKey(Category)

