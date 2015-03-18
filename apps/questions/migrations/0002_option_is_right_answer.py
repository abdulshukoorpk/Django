# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='is_right_answer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
