# Generated by Django 4.1.7 on 2023-03-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userpersonalinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='url_username',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]
