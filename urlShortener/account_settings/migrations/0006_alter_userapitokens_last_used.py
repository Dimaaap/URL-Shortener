# Generated by Django 4.1.7 on 2023-05-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_settings', '0005_remove_userapitokens_token_opportunity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapitokens',
            name='last_used',
            field=models.DateTimeField(blank=True, null=None),
        ),
    ]
