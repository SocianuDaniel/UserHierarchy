# Generated by Django 5.1.1 on 2024-10-05 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='level',
        ),
    ]