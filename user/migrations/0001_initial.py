# Generated by Django 2.2.7 on 2019-11-25 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Fifth Year')])),
                ('total_students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Year')),
            ],
        ),
    ]
