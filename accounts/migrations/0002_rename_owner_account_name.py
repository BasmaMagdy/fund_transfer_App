# Generated by Django 4.2.3 on 2024-12-17 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='owner',
            new_name='name',
        ),
    ]