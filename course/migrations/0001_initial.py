# Generated by Django 4.2.7 on 2023-12-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=50, unique=True)),
                ('coursecode', models.IntegerField()),
                ('courseDuration', models.CharField(max_length=50)),
            ],
        ),
    ]
