# Generated by Django 3.2 on 2021-05-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_charity_default_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
