# Generated by Django 4.0.5 on 2022-06-28 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_basiccv_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basiccv',
            name='cv_number',
        ),
    ]
