# Generated by Django 2.2.10 on 2020-06-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_orders_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('message', models.TextField(default='', max_length=1000)),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]