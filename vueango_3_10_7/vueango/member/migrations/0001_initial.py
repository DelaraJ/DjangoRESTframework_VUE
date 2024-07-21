# Generated by Django 5.0.7 on 2024-07-19 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=225)),
                ('lastname', models.CharField(max_length=225)),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('status', models.CharField(choices=[('member', 'Member'), ('saved', 'Saved')], default='member', max_length=10)),
            ],
        ),
    ]