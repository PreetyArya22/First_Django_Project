# Generated by Django 5.1.5 on 2025-02-05 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'managed': False, 'ordering': ['age']},
        ),
    ]
