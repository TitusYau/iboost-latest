# Generated by Django 4.2.2 on 2023-06-26 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0026_srr_profile"),
        ("teacherui", "0009_remove_student_srr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="profile",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dashboard.profile",
            ),
        ),
    ]
