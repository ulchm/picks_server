# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('starts_at', models.DateTimeField()),
                ('is_playing', models.BooleanField(default=False)),
                ('home_score', models.IntegerField(null=True, blank=True)),
                ('away_score', models.IntegerField(null=True, blank=True)),
                ('period', models.CharField(max_length=255, null=True, blank=True)),
                ('is_final', models.BooleanField(default=False)),
                ('was_shootout', models.BooleanField(default=False)),
                ('was_overtime', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of the season.', max_length=255)),
                ('start_date', models.DateField(help_text=b'The first day of the season.')),
                ('end_date', models.DateField(help_text=b'The last day of the season')),
                ('is_active', models.BooleanField(default=True)),
                ('league', models.ForeignKey(related_name='seasons', to='schedule.League')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of the team, without the city', max_length=255)),
                ('short_name', models.CharField(help_text=b'The short name / code for the team.  3 Letters.', max_length=3)),
                ('city', models.CharField(help_text=b'The city the team is from', max_length=255, null=True, blank=True)),
                ('large_logo', models.ImageField(null=True, upload_to=b'team_large_logos', blank=True)),
                ('small_logo', models.ImageField(null=True, upload_to=b'team_small_logos', blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(related_name='away_games', to='schedule.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(related_name='home_games', to='schedule.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='losing_team',
            field=models.ForeignKey(related_name='games_lost', blank=True, to='schedule.Team', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(related_name='games', to='schedule.Season'),
        ),
        migrations.AddField(
            model_name='game',
            name='winning_team',
            field=models.ForeignKey(related_name='games_won', blank=True, to='schedule.Team', null=True),
        ),
    ]
