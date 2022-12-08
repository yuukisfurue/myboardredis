# Generated by Django 3.2.12 on 2022-12-08 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('jyob', models.CharField(max_length=100)),
            ],
        ),
    ]
