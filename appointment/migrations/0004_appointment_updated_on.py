# Generated by Django 4.2.13 on 2024-07-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_alter_appointment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
