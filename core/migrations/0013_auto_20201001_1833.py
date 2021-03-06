# Generated by Django 3.1.1 on 2020-10-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_recentwork_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='experience',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recentwork',
            name='demo',
            field=models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='site'),
        ),
    ]
