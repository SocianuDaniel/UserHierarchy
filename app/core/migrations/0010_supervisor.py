# Generated by Django 5.1.2 on 2024-10-23 20:41

import core.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_owner_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('level', models.PositiveIntegerField(choices=[(0, 'Root'), (1, 'Owner'), (2, 'Supervisor')], validators=[core.models.validateEqual], verbose_name='user level')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.owner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]