# Generated by Django 5.0.6 on 2024-07-28 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='brand',
            new_name='category',
        ),
    ]