# Generated by Django 3.2.12 on 2023-05-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation_id',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employees',
        ),
    ]