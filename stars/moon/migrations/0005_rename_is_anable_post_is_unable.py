# Generated by Django 4.1.3 on 2022-12-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_anable',
            new_name='is_unable',
        ),
    ]
