# Generated by Django 3.1.8 on 2021-06-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DakaLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
                ('log', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DakaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=10)),
                ('openid', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=8)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]