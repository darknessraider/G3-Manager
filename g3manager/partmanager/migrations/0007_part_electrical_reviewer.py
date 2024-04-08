# Generated by Django 5.0.4 on 2024-04-08 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('partmanager', '0006_remove_part_builder_remove_part_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='electrical_reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='electrical_reviewer', to='home.member'),
        ),
    ]