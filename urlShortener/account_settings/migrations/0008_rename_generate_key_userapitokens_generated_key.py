# Generated by Django 4.1.7 on 2023-06-08 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_settings', '0007_alter_userapitokens_generate_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userapitokens',
            old_name='generate_key',
            new_name='generated_key',
        ),
    ]