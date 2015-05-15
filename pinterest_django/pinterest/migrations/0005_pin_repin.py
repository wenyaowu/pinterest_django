# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0004_auto_20150514_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='repin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
