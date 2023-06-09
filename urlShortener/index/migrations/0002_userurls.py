# Generated by Django 4.1.7 on 2023-06-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.GenericIPAddressField()),
                ('long_url', models.URLField()),
                ('shorten_url', models.URLField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='site-image/%Y/%m/%d')),
            ],
        ),
    ]
