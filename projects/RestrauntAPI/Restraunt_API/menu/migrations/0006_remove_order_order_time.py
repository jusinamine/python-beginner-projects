# Generated by Django 3.2.7 on 2022-06-01 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0005_rename_email_order_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_time",
        ),
    ]
