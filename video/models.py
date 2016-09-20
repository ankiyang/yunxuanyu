# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from category.models import Category


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