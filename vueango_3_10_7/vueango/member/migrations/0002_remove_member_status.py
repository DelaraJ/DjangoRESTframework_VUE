# Generated by Django 5.0.7 on 2024-07-19 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='status',
        ),
    ]