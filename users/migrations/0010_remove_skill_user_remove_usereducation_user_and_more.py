# Generated by Django 4.2.8 on 2024-05-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_users_languagecv_languagecv_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usereducation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userpersonalinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='user',
        ),
        migrations.AddField(
            model_name='skill',
            name='user_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usereducation',
            name='user_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='userpersonalinfo',
            name='user_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='user_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
