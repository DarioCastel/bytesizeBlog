# Generated by Django 5.1.2 on 2024-10-24 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_rename_email_contacto_emai'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='emai',
            new_name='email',
        ),
    ]
