# Generated by Django 5.0.6 on 2024-07-02 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restarant', '0003_signup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='full_name',
            new_name='fullname',
        ),
    ]
