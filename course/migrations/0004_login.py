# Generated by Django 4.2.7 on 2024-01-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
