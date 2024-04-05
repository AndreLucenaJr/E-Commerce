# Generated by Django 5.0.4 on 2024-04-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao_curta', models.TextField(max_length=255)),
                ('descricao_longa', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m')),
                ('slug', models.SlugField(unique=True)),
                ('preco', models.FloatField(default=0)),
                ('preco_promocional', models.FloatField(default=0)),
                ('tipo', models.CharField(choices=[('V', 'Variáveis'), ('S', 'Simples')], default='V', max_length=1)),
            ],
        ),
    ]
