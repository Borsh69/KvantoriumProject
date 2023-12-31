# Generated by Django 4.2.1 on 2023-05-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_buy_shop_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=50)),
                ('dayWeek', models.CharField(max_length=50)),
                ('time', models.TimeField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='projects',
            field=models.ManyToManyField(null=True, to='base.project'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('timetable', models.ManyToManyField(to='base.timetable', verbose_name='Дни учёбы')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='group',
            field=models.ManyToManyField(null=True, to='base.group'),
        ),
    ]
