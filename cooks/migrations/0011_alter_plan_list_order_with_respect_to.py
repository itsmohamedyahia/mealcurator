# Generated by Django 4.0.1 on 2022-09-11 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooks', '0010_plan_list'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='plan_list',
            order_with_respect_to='meal',
        ),
    ]