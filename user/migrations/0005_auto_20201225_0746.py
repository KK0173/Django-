# Generated by Django 3.1.4 on 2020-12-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201225_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='password',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='test',
            name='tel',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterModelTable(
            name='test',
            table=None,
        ),
    ]
