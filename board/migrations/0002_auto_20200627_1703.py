# Generated by Django 3.0.7 on 2020-06-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='OS',
            field=models.CharField(choices=[('etc', '기타'), ('software', '소프트웨어'), ('hardware', '하드웨어')], max_length=80, null=True),
        ),
    ]
