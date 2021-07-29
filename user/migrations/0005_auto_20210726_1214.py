# Generated by Django 3.1.8 on 2021-07-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210602_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=64)),
                ('unionid', models.CharField(max_length=64)),
                ('nick_name', models.TextField()),
                ('city', models.TextField()),
                ('avatar', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='loginstate',
            name='openid',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='loginstate',
            name='type',
            field=models.IntegerField(db_index=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loginstate',
            name='student_id',
            field=models.IntegerField(null=True),
        ),
    ]
