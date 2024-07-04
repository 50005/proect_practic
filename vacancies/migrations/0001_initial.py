# Generated by Django 5.0.6 on 2024-06-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hh_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('salary_from', models.FloatField(blank=True, null=True)),
                ('salary_to', models.FloatField(blank=True, null=True)),
                ('working_days', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
