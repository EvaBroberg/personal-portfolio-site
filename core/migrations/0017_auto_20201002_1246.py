# Generated by Django 3.1.1 on 2020-10-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_journey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='modal',
            field=models.TextField(blank=True, verbose_name='Work description'),
        ),
        migrations.AlterField(
            model_name='recentwork',
            name='description',
            field=models.TextField(blank=True, verbose_name='Work description'),
        ),
    ]
