# Generated by Django 5.1.3 on 2024-11-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("custom_messages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="message_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
