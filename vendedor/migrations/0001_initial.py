# Generated by Django 2.2.3 on 2019-07-08 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=30, verbose_name='Sobrenome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('plano_comissoes', models.CharField(max_length=80, verbose_name='Comissoes')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
                'ordering': ['nome', 'plano_comissoes', 'idade'],
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(max_length=2, verbose_name='DDD')),
                ('numero_telefone', models.CharField(max_length=15, verbose_name='Numero')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone_vendedor', to='vendedor.Vendedor', verbose_name='Vendedor')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
                'ordering': ['ddd', 'numero_telefone'],
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=10, verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=150, verbose_name='Estado')),
                ('pais', models.CharField(default='Brasil', max_length=150, verbose_name='País')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedor', to='vendedor.Vendedor', verbose_name='Vendedor')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endreços',
                'ordering': ['cidade', 'estado'],
            },
        ),
    ]