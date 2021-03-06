# Generated by Django 3.1.1 on 2020-11-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20201102_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='company_image2',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_image3',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_image4',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
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
            name='job_description2',
            field=models.TextField(blank=True, verbose_name='job description'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_description3',
            field=models.TextField(blank=True, verbose_name='job description'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_description4',
            field=models.TextField(blank=True, verbose_name='job description'),
        ),
    ]
