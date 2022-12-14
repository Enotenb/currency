# Generated by Django 4.1 on 2022-08-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=254)),
                ('email_to', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
    ]
