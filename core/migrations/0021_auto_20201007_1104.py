# Generated by Django 3.1.1 on 2020-10-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20201002_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='modal',
        ),
        migrations.AddField(
            model_name='journey',
            name='company_image',
            field=models.ImageField(blank=True, upload_to='journey'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_image2',
            field=models.ImageField(blank=True, upload_to='journey'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_image3',
            field=models.ImageField(blank=True, upload_to='journey'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_image4',
            field=models.ImageField(blank=True, upload_to='journey'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_name',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_name2',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_name3',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_name4',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_date',
            field=models.CharField(blank=True, max_length=100, verbose_name='job date'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_date2',
            field=models.CharField(blank=True, max_length=100, verbose_name='job date'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_date3',
            field=models.CharField(blank=True, max_length=100, verbose_name='job date'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_date4',
            field=models.CharField(blank=True, max_length=100, verbose_name='job date'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_description',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_description2',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_description3',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_description4',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='recentwork',
            name='description',
            field=models.TextField(blank=True, verbose_name='Work description'),
        ),
    ]
