# Generated by Django 3.2.7 on 2021-09-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signuppage', '0003_alter_signuppage_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signuppage',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
