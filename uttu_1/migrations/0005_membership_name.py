# Generated by Django 3.0.4 on 2020-03-16 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uttu_1', '0004_auto_20200316_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
