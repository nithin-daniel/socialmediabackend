# Generated by Django 5.0.2 on 2024-02-23 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='comment',
            new_name='post',
        ),
    ]
