# Generated by Django 4.2.5 on 2023-09-14 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_account_request_buy'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('email', 'login', 'password', 'age', 'name')},
        ),
        migrations.RemoveField(
            model_name='account',
            name='teacher',
        ),
    ]
