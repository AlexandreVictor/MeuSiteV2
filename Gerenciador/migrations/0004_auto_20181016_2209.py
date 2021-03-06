# Generated by Django 2.1.2 on 2018-10-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gerenciador', '0003_auto_20181014_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='complemento',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='advogado',
            field=models.BooleanField(default=False, verbose_name='Tem advogado ?'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='segredo',
            field=models.BooleanField(default=False, verbose_name='É segredo ?'),
        ),
    ]
