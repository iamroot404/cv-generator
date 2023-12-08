# Generated by Django 4.0.5 on 2022-06-26 10:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicCv',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('idno', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('nation', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('university', models.CharField(blank=True, max_length=200)),
                ('university_year', models.CharField(blank=True, max_length=50)),
                ('university_course', models.CharField(blank=True, max_length=200)),
                ('highschool', models.CharField(max_length=200)),
                ('highschool_year', models.CharField(max_length=50)),
                ('highschool_cert', models.CharField(max_length=200)),
                ('primary', models.CharField(max_length=200)),
                ('primary_year', models.CharField(max_length=50)),
                ('primary_cert', models.CharField(max_length=200)),
                ('skill_one', models.CharField(max_length=50)),
                ('skill_two', models.CharField(max_length=50)),
                ('skill_three', models.CharField(max_length=50)),
                ('hobby_one', models.CharField(max_length=50)),
                ('hobby_two', models.CharField(max_length=50)),
                ('hobby_three', models.CharField(max_length=50)),
                ('referee_name_one', models.CharField(max_length=50)),
                ('referee_contact_one', models.CharField(max_length=20)),
                ('referee_post_one', models.CharField(max_length=200)),
                ('referee_company_one', models.CharField(max_length=200)),
                ('referee_name_two', models.CharField(max_length=50)),
                ('referee_contact_two', models.CharField(max_length=20)),
                ('referee_post_two', models.CharField(max_length=200)),
                ('referee_company_two', models.CharField(max_length=200)),
                ('referee_name_three', models.CharField(blank=True, max_length=50)),
                ('referee_contact_three', models.CharField(blank=True, max_length=20)),
                ('referee_post_three', models.CharField(blank=True, max_length=200)),
                ('referee_company_three', models.CharField(blank=True, max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]