# Generated by Django 2.1.2 on 2018-10-13 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reu', models.CharField(max_length=200)),
                ('documento', models.CharField(max_length=14)),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('cep', models.IntegerField()),
                ('numero_processo', models.IntegerField()),
                ('segredo', models.IntegerField(default=0)),
                ('data_inclusao', models.DateTimeField(auto_now=True)),
                ('fk_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gerenciador.autor')),
            ],
        ),
        migrations.CreateModel(
            name='statusgeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('status_acompanhamento', models.CharField(max_length=20)),
                ('fk_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gerenciador.autor')),
                ('fk_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gerenciador.cadastro')),
            ],
        ),
    ]
