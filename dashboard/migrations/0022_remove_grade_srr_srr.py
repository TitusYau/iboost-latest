# Generated by Django 4.0.3 on 2023-06-23 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_alter_grade_avg_alter_subject_subjectavg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='srr',
        ),
        migrations.CreateModel(
            name='SRR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srr', models.TextField(max_length=1000, null=True)),
                ('title', models.TextField(max_length=100, null=True)),
                ('bestatl', models.BooleanField()),
                ('worstatl', models.BooleanField()),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.grade')),
            ],
        ),
    ]
