# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(0, b'Public'), (100, b'Private')])),
                ('password', models.CharField(max_length=255, null=True, blank=True)),
                ('registration_opens_at', models.DateTimeField(default=datetime.datetime(2015, 11, 12, 21, 53, 49, 512674, tzinfo=utc))),
                ('pick_locking_type', models.CharField(max_length=b'1', choices=[(b'd', b'Daily at set time'), (b'w', b'Weekly at a set time'), (b'm', b'Minutes before the game starts')])),
                ('games_to_include', models.CharField(max_length=b'3', choices=[(b'All', b'All Games'), (b'd2d', b'DOTW to DOTW (e.g. Thurs to Sun'), (b'date', b'Only date to date')])),
                ('scoring_method', models.CharField(max_length=b'1', choices=[(b'T', b'Traditional - 2 for win, 1 for OT loss, 0 for reg loss'), (b'M', b'Modified - 3 for reg win, 2 for OT win, 1 for SO win, 0 for loss.'), (b'P', b'Precision - 3 for SO win, 2 for OT win, 1 for reg win, 0 for loss.')])),
                ('allow_forgot_picks_notifications', models.BooleanField(default=True)),
                ('show_others_picks', models.BooleanField(default=True)),
                ('allow_manual_lock', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(related_name='pools_created', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='pools_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
