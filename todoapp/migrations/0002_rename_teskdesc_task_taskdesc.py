# Generated by Django 4.0.4 on 2022-06-07 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='teskDesc',
            new_name='taskDesc',
        ),
    ]
