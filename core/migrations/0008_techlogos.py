# Generated by Django 3.1.1 on 2020-10-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201001_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechLogos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tech-logos')),
            ],
        ),
    ]