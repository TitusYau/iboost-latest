# Generated by Django 4.0.3 on 2023-06-23 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_alter_srr_bestatl_alter_srr_worstatl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srr',
            name='grade',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.grade'),
        ),
    ]