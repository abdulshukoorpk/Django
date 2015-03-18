# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20150311_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='exam1',
            new_name='exam',
        ),
    ]
