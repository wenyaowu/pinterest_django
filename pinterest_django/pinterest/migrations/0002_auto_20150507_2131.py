# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name=models.CharField(max_length=256)),
        ),
    ]
