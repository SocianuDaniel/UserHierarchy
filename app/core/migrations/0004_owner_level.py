# Generated by Django 5.1.1 on 2024-10-05 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_owner_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='level',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='user level'),
            preserve_default=False,
        ),
    ]