# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20150305_0549'),
        ('exams', '0002_auto_20150305_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.ForeignKey(related_name='answers', default=1, to='questions.Option'),
            preserve_default=False,
        ),
    ]
