# Generated by Django 4.0 on 2021-12-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruit',
            old_name='content',
            new_name='discription',
        ),
    ]