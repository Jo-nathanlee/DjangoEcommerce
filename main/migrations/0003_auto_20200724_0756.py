# Generated by Django 3.0.8 on 2020-07-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bank_account',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
