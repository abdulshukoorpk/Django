# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ManyToManyField(related_name='answers', to='questions.Question'),
            preserve_default=True,
        ),
    ]
