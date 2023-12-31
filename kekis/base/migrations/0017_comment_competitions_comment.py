# Generated by Django 4.2.4 on 2023-12-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_remove_project_addition_project_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.account')),
            ],
        ),
        migrations.AddField(
            model_name='competitions',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='base.comment'),
        ),
    ]
