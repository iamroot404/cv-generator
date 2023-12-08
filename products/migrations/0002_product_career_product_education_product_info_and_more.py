# Generated by Django 4.0.5 on 2022-08-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='career',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='education',
            field=models.CharField(default='Educational Background', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(default='Personal Information', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='ref',
            field=models.CharField(default='Referee', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='skills',
            field=models.CharField(default='Skills And Hobbies', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='work',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
