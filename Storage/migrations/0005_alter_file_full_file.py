# Generated by Django 4.2.5 on 2023-12-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0004_remove_file_author_alter_file_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='full_file',
            field=models.FileField(upload_to=''),
        ),
    ]
