# Generated by Django 5.0.3 on 2024-03-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.CharField(max_length=155)),
                ('designer', models.CharField(max_length=155)),
                ('year_released', models.IntegerField(max_length=4)),
                ('players', models.IntegerField(max_length=2)),
                ('completion_time', models.IntegerField(max_length=2)),
                ('min_age', models.ImageField(max_length=2, upload_to='')),
            ],
        ),
    ]
