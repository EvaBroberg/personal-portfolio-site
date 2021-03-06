# Generated by Django 3.1.1 on 2020-11-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20201105_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Work title')),
                ('client', models.TextField(blank=True, verbose_name='Client')),
                ('description', models.TextField(blank=True, verbose_name='Work description')),
                ('work_description', models.TextField(blank=True, verbose_name='Work responsibilities')),
                ('image', models.ImageField(upload_to='works')),
                ('code', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='code')),
                ('demo', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='demo')),
                ('site', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='site')),
            ],
        ),
    ]
