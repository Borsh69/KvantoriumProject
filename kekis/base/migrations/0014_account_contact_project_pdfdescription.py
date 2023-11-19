# Generated by Django 4.2.6 on 2023-11-19 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_account_group_remove_account_isteacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='contact',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='PDFdescription',
            field=models.FileField(blank=True, null=True, upload_to='pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
