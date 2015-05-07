# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0003_test_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(related_name='answers', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
