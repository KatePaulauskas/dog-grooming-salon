# Generated by Django 4.2.13 on 2024-06-05 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact_request', '0002_alter_contactrequest_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]