# Generated by Django 4.0.4 on 2022-06-29 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='urn',
            new_name='user',
        ),
    ]
