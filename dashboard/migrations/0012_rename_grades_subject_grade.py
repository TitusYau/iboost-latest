# Generated by Django 4.0.3 on 2023-01-01 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_profile_userid_profile_email_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='grades',
            new_name='grade',
        ),
    ]
