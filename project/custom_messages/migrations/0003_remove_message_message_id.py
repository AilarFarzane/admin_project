# Generated by Django 5.1.3 on 2024-11-21 13:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("custom_messages", "0002_alter_message_message_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="message_id",
        ),
    ]
