# Generated by Django 5.0.2 on 2024-02-22 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_logentry_loguser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logentry',
            old_name='logUser',
            new_name='User',
        ),
    ]
