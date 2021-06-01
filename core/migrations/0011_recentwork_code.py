# Generated by Django 3.1.1 on 2020-10-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_delete_techlogos'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentwork',
            name='code',
            field=models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='code'),
        ),
    ]