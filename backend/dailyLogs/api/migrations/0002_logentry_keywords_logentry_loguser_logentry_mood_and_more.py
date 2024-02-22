# Generated by Django 5.0.2 on 2024-02-22 11:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='logUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logOfUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='logentry',
            name='mood',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='logentry',
            name='summary',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]
