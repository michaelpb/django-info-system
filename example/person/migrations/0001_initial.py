# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_info_system.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, default='', help_text='Notes or description', verbose_name='Description')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('account', models.OneToOneField(blank=True, help_text='Account associated with profile', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='associated_person', to=settings.AUTH_USER_MODEL, verbose_name='Account')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'get_latest_by': 'updated_date',
                'abstract': False,
            },
            bases=(models.Model, django_info_system.models.UpdateMixin),
        ),
    ]
