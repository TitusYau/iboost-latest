# Generated by Django 4.0.3 on 2023-01-21 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_subject_srr_grade_srr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
