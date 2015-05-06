# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_answer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
    ]
