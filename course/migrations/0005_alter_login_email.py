# Generated by Django 4.2.7 on 2024-01-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]