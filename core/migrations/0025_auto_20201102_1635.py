# Generated by Django 3.1.1 on 2020-11-02 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20201024_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='company_image2',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='company_image3',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='company_image4',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='company_name2',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='company_name3',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='company_name4',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='job_date2',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='job_date3',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='job_date4',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='job_description2',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='job_description3',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='job_description4',
        ),
    ]
