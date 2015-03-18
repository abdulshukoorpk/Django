# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_test_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='exam',
        ),
        migrations.AddField(
            model_name='test',
            name='exam1',
            field=models.ForeignKey(related_name='tests1', default=1, to='exams.Exam'),
            preserve_default=False,
        ),
    ]
