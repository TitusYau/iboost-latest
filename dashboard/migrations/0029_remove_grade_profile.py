# Generated by Django 4.0.3 on 2023-08-02 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_grade_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='profile',
        ),
    ]
