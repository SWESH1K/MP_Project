# Generated by Django 5.1.6 on 2025-02-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_classes_class_rename_subjects_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
