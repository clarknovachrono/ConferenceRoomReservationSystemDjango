# Generated by Django 3.2 on 2022-03-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_room_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.AddField(
            model_name='room',
            name='image_url',
            field=models.CharField(default='', max_length=2083),
        ),
    ]
