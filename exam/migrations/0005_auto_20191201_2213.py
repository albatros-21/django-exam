# Generated by Django 2.2.7 on 2019-12-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(default=1)),
                ('exam_id', models.IntegerField(default=1)),
                ('mark', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='user_id',
            new_name='student_id',
        ),
    ]
