# Generated by Django 3.1.1 on 2020-11-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20201105_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentwork',
            name='client',
            field=models.TextField(blank=True, verbose_name='Client'),
        ),
        migrations.AddField(
            model_name='recentwork',
            name='work_description',
            field=models.TextField(blank=True, verbose_name='Client'),
        ),
    ]
