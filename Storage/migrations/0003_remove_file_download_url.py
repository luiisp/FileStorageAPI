# Generated by Django 5.0 on 2023-12-28 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0002_file_download_url_file_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='download_url',
        ),
    ]
