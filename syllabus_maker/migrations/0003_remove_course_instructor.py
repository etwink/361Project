# Generated by Django 3.1.3 on 2020-12-08 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_maker', '0002_auto_20201206_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
    ]
