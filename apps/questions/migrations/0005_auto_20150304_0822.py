# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20150304_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='option',
            new_name='option_text',
        ),
    ]
