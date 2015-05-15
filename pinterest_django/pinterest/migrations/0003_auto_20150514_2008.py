# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0002_auto_20150513_0629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pin',
            options={'ordering': ['-id']},
        ),
    ]
