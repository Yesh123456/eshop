# Generated by Django 3.2.8 on 2021-11-09 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=14),
            preserve_default=False,
        ),
    ]
