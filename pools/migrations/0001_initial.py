# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(0, b'Public'), (100, b'Private')])),
                ('password', models.CharField(max_length=255, null=True, blank=True)),
                ('registration_opens_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('pick_locking_type', models.IntegerField(choices=[(1, b'Daily at set time'), (2, b'Weekly at a set time'), (3, b'Minutes before the game starts')])),
                ('games_to_include', models.IntegerField(choices=[(1, b'All Games'), (2, b'DOTW to DOTW (e.g. Thurs to Sun'), (3, b'Only date to date')])),
                ('scoring_method', models.IntegerField(choices=[(1, b'Traditional - 2 for win, 1 for OT loss, 0 for reg loss'), (2, b'Modified - 3 for reg win, 2 for OT win, 1 for SO win, 0 for loss.'), (3, b'Precision - 3 for SO win, 2 for OT win, 1 for reg win, 0 for loss.')])),
                ('allow_forgot_picks_notifications', models.BooleanField(default=True)),
                ('show_others_picks', models.BooleanField(default=True)),
                ('allow_manual_lock', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(related_name='pools_created', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='pools_joined', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('season', models.ForeignKey(related_name='pools', to='schedule.Season')),
            ],
        ),
        migrations.AddField(
            model_name='pick',
            name='pool',
            field=models.ForeignKey(related_name='picks', to='pools.Pool'),
        ),
        migrations.AddField(
            model_name='pick',
            name='user',
            field=models.ForeignKey(related_name='picks', to=settings.AUTH_USER_MODEL),
        ),
    ]
