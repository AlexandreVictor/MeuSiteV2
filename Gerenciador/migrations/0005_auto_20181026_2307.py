# Generated by Django 2.1.2 on 2018-10-27 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gerenciador', '0004_auto_20181016_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='advogado',
            field=models.IntegerField(default=0, verbose_name='Tem advogado ?'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='segredo',
            field=models.IntegerField(default=0, verbose_name='Segredo ?'),
        ),
    ]