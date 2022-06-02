# Generated by Django 4.0.4 on 2022-06-02 14:48

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MarketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.CharField(max_length=200)),
                ('item_price', models.DecimalField(decimal_places=2, default=1.0, max_digits=7, validators=[django.core.validators.MinValueValidator(1)])),
                ('item_quantity', models.PositiveIntegerField(default=1)),
                ('item_infinite', models.BooleanField(default=False)),
                ('item_is_featured', models.BooleanField(default=False)),
                ('item_date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('item_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.category')),
                ('item_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Market Item',
                'verbose_name_plural': 'Market Items',
            },
        ),
    ]