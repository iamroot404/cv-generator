# Generated by Django 4.0.5 on 2022-08-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0009_advancedbasic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedbasic',
            name='career',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
