# Generated by Django 5.1.1 on 2024-10-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_owner_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='level',
            field=models.PositiveBigIntegerField(default=1, verbose_name='user level'),
        ),
    ]
