# Generated by Django 3.2 on 2022-03-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20220316_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image_url',
            field=models.CharField(default='', max_length=2083),
        ),
    ]
