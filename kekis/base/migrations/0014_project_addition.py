# Generated by Django 4.2.6 on 2023-11-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_account_group_remove_account_isteacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='addition',
            field=models.FileField(blank=True, upload_to='files/', verbose_name='Addition'),
        ),
    ]
