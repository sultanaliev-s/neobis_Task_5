# Generated by Django 3.1 on 2020-08-29 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepercentage',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicepercentage',
            name='percentage',
            field=models.IntegerField(verbose_name='percentage for the service'),
        ),
    ]