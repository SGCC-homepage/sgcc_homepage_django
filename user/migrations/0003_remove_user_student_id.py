# Generated by Django 3.1.7 on 2021-03-05 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210305_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='student_id',
        ),
    ]
