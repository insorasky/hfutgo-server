# Generated by Django 3.1.7 on 2021-04-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField(db_index=True)),
                ('sname', models.TextField()),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('code', models.CharField(db_index=True, max_length=20)),
                ('credit', models.IntegerField(db_index=True)),
                ('classcode', models.TextField()),
                ('classname', models.CharField(db_index=True, max_length=80)),
                ('type', models.CharField(db_index=True, max_length=30)),
                ('department', models.CharField(db_index=True, max_length=50)),
                ('teacher', models.CharField(db_index=True, max_length=50)),
                ('info', models.JSONField()),
                ('campus', models.CharField(db_index=True, max_length=15)),
                ('lessons', models.IntegerField(db_index=True)),
                ('weeks', models.IntegerField(db_index=True)),
                ('weeklessons', models.IntegerField(db_index=True)),
                ('personlimit', models.IntegerField(db_index=True)),
            ],
        ),
    ]