# Generated by Django 2.1.1 on 2018-10-11 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_auto_20181011_1835'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contests',
            new_name='Contest',
        ),
        migrations.RenameModel(
            old_name='Problems',
            new_name='Problem',
        ),
    ]
