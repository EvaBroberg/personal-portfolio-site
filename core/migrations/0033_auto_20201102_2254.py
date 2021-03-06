# Generated by Django 3.1.1 on 2020-11-02 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20201102_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journey',
            options={'verbose_name': 'Journey', 'verbose_name_plural': 'Journey'},
        ),
        migrations.AddField(
            model_name='journey',
            name='company_image',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
        ),
        migrations.AddField(
            model_name='journey',
            name='company_name',
            field=models.TextField(blank=True, verbose_name='company name'),
        ),
        migrations.AddField(
            model_name='journey',
            name='date',
            field=models.CharField(blank=True, max_length=100, verbose_name='date'),
        ),
        migrations.AddField(
            model_name='journey',
            name='image',
            field=models.ImageField(blank=True, upload_to='journey'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_date',
            field=models.CharField(blank=True, max_length=100, verbose_name='job date'),
        ),
        migrations.AddField(
            model_name='journey',
            name='job_title',
            field=models.TextField(blank=True, verbose_name='job title'),
        ),
        migrations.AlterField(
            model_name='duties',
            name='duty',
            field=models.CharField(blank=True, max_length=100, verbose_name='duty'),
        ),
    ]
