# Generated by Django 2.2.14 on 2020-07-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
