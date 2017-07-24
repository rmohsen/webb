# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 01:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('P1', '0005_comment_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='std_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='std_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post_word',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='P1.Post'),
        ),
    ]