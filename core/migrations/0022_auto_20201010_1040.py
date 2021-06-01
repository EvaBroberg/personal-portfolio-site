# Generated by Django 3.1.1 on 2020-10-10 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20201007_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='company_image',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='company_image2',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='company_image3',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='company_image4',
            field=models.ImageField(blank=True, upload_to='journey', verbose_name='company image'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='job_description',
            field=models.TextField(blank=True, verbose_name='job description'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='job_description2',
            field=models.TextField(blank=True, verbose_name='job description'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='job_description3',
            field=models.TextField(blank=True, verbose_name='job description'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='job_description4',
            field=models.TextField(blank=True, verbose_name='job description'),
        ),
        migrations.CreateModel(
            name='SkillsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('Skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.skills')),
            ],
        ),
    ]