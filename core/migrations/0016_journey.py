# Generated by Django 3.1.1 on 2020-10-01 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20201001_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='site')),
                ('image', models.ImageField(upload_to='journey')),
                ('date', models.CharField(max_length=100, verbose_name='date')),
            ],
            options={
                'verbose_name': 'Journey',
                'verbose_name_plural': 'Journey',
            },
        ),
    ]
