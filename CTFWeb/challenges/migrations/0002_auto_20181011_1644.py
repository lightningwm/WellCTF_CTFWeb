# Generated by Django 2.1.1 on 2018-10-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solved',
            name='problem_id',
            field=models.IntegerField(max_length=250),
        ),
        migrations.AlterField(
            model_name='solved',
            name='user_id',
            field=models.IntegerField(max_length=250),
        ),
    ]
