# Generated by Django 2.0.7 on 2018-08-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20180803_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='imposto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='venda',
            name='numero',
            field=models.IntegerField(auto_created=True, unique=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]