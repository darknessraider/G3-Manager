# Generated by Django 5.0.4 on 2024-04-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partmanager', '0004_part_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]