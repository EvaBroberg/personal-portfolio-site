# Generated by Django 3.1.1 on 2020-11-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20201102_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='job_title',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_title2',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_title3',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_title4',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
    ]
