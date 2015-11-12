# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pool',
            name='registration_opens_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 21, 54, 32, 90848, tzinfo=utc)),
        ),
    ]
