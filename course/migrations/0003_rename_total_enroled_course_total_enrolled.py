# Generated by Django 4.2.15 on 2024-08-10 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_lession_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='total_enroled',
            new_name='total_enrolled',
        ),
    ]
