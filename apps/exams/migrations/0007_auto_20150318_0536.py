# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20150311_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='option',
            new_name='selected_option',
        ),
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(related_name='answers', default=1, to='exams.Test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='exam',
            field=models.ForeignKey(related_name='tests', to='exams.Exam'),
            preserve_default=True,
        ),
    ]
