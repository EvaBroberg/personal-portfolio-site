# Generated by Django 3.1.1 on 2020-10-24 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20201011_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codinglanguagesimage',
            name='CodingLanguages',
        ),
        migrations.DeleteModel(
            name='CodingLanguages',
        ),
        migrations.DeleteModel(
            name='CodingLanguagesImage',
        ),
    ]