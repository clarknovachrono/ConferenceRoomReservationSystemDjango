# Generated by Django 3.2 on 2022-03-21 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_reservation_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='date',
            new_name='date_field',
        ),
    ]
