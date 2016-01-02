# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoolInvitations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('accepted_at', models.DateTimeField(null=True, blank=True)),
                ('invited_by', models.ForeignKey(related_name='pool_invitations_sent', to=settings.AUTH_USER_MODEL)),
                ('pool', models.ForeignKey(related_name='invitations', to='pools.Pool')),
                ('sent_to', models.ForeignKey(related_name='pool_invitations_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
