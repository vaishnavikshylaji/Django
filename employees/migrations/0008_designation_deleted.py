# Generated by Django 3.2.12 on 2023-05-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20230523_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
