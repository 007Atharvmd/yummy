# Generated by Django 5.1.5 on 2025-04-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_booking_table_people_alter_booking_table_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_table',
            name='message',
            field=models.CharField(default='HEllo', max_length=255),
            preserve_default=False,
        ),
    ]
