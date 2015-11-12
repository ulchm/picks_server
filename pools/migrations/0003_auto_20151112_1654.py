# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0002_auto_20151112_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='registration_opens_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
