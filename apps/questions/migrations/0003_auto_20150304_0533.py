# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_option_is_right_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='is_right_answer',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
