# Generated by Django 2.2.7 on 2021-02-23 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0024_auto_20210223_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice_id',
            field=models.IntegerField(),
        ),
    ]
