# Generated by Django 5.1.5 on 2025-02-04 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_human_alter_articles_reporters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='reporters',
        ),
        migrations.RemoveField(
            model_name='toyota',
            name='car',
        ),
        migrations.RemoveField(
            model_name='category',
            name='fruit',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='members',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='car',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='persons',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Person_Choice',
        ),
        migrations.DeleteModel(
            name='Runner',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Fruit',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
        migrations.DeleteModel(
            name='Manufacture',
        ),
        migrations.DeleteModel(
            name='Toyota',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Persons',
        ),
    ]
