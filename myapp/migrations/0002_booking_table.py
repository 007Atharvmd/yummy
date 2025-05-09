# Generated by Django 5.1.5 on 2025-04-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('date', models.DateField(max_length=255)),
                ('time', models.TimeField(max_length=255)),
                ('people', models.IntegerField(max_length=255)),
                ('phone', models.IntegerField(max_length=13)),
            ],
        ),
    ]
