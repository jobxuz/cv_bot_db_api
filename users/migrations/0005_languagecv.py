# Generated by Django 4.2.8 on 2024-05-17 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_workexperience_usereducation_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageCv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
