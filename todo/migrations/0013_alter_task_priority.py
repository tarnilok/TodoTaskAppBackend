# Generated by Django 4.0.1 on 2022-01-31 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('high priority', '3'), ('medium priority', '2'), ('low priority', '1'), ('no priority', '0')], default='0', max_length=20),
        ),
    ]
