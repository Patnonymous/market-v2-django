# Generated by Django 4.0.4 on 2022-06-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
