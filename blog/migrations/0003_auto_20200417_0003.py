# Generated by Django 3.0.3 on 2020-04-16 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200416_0102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogProject',
            new_name='Blog',
        ),
    ]
