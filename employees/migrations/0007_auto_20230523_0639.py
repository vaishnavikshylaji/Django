# Generated by Django 3.2.12 on 2023-05-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20230523_0622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='designation_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.designation'),
        ),
    ]
