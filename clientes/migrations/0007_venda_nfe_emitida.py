# Generated by Django 2.0.7 on 2018-08-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20180730_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='nfe_emitida',
            field=models.BooleanField(default=False),
        ),
    ]
