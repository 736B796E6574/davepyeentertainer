# Generated by Django 5.0 on 2024-01-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('live_url', models.URLField()),
            ],
        ),
    ]
