# Generated by Django 2.0.7 on 2018-08-03 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0009_auto_20180803_1934'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensDoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('imposto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nfe_emitida', models.BooleanField(default=False)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='itensdopedido',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Venda'),
        ),
    ]
