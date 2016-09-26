# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u89c6\u9891\u4f5c\u8005', 'verbose_name_plural': '\u89c6\u9891\u4f5c\u8005'},
        ),
        migrations.AddField(
            model_name='video',
            name='click_num',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
    ]
