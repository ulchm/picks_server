# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pools', '0003_auto_20151112_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('game', models.ForeignKey(related_name='picks', to='schedule.Game')),
                ('pick', models.ForeignKey(related_name='picks', to='schedule.Team')),
                ('pool', models.ForeignKey(related_name='picks', to='pools.Pool')),
                ('user', models.ForeignKey(related_name='picks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
