# Generated by Django 4.0.5 on 2022-08-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_career_product_education_product_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(default='basic', max_length=200),
        ),
    ]
