# Generated by Django 4.0.3 on 2022-04-08 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_servico', models.CharField(max_length=60)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('creation_date', models.DateTimeField(verbose_name='Criadoem')),
            ],
        ),
    ]
