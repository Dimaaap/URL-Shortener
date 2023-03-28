# Generated by Django 4.1.7 on 2023-03-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userpersonalinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='avatars/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='UserPersonalInfo',
        ),
    ]