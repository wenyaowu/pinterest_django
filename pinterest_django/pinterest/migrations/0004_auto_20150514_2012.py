# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0003_auto_20150514_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pin',
            options={'ordering': ['-pk']},
        ),
    ]
