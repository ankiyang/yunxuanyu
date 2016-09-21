# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(u"名字", max_length=30)
    desc = models.CharField(u"描述", max_length=150)
    manager = models.ForeignKey(User, verbose_name="作者")

    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"


class Video(models.Model):
    category = models.ForeignKey(Category, verbose_name=u"所属类别")
    owner = models.ForeignKey(User, verbose_name=u"作者")
    title = models.CharField(u"标题", max_length=100)
    content = models.CharField(u"视频内容", max_length=100000)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = u"视频"