# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20150311_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='option',
            new_name='selected_option',
        ),
        migrations.RemoveField(
            model_name='test',
            name='exam1',
        ),
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(related_name='answers', default=1, to='exams.Test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='exam',
            field=models.ForeignKey(related_name='tests', default=1, to='exams.Exam'),
            preserve_default=False,
        ),
    ]
