# Generated by Django 5.0.6 on 2024-05-15 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_deployment_file_to_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deployment',
            old_name='Your_name',
            new_name='Your_Name',
        ),
    ]