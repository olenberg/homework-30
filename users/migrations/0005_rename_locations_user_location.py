# Generated by Django 4.1.7 on 2023-04-27 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='locations',
            new_name='location',
        ),
    ]
