# Generated by Django 3.2.7 on 2021-09-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signuppage', '0002_auto_20210928_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signuppage',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]