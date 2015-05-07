# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, b'not started'), (1, b'Active'), (2, b'Completed')]),
            preserve_default=False,
        ),
    ]
