# Generated by Django 3.1.4 on 2020-12-25 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201225_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='password',
        ),
        migrations.RemoveField(
            model_name='test',
            name='tel',
        ),
    ]
