# Generated by Django 4.1.7 on 2023-03-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_url_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonalinfo',
            name='avatar',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='avatars/%Y/%m/%d'),
        ),
    ]
