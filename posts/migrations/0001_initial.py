# Generated by Django 2.1.2 on 2018-10-10 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('subtitulo', models.CharField(max_length=255, verbose_name='sub-titulo')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('conteudo', models.TextField()),
                ('categorias', models.ManyToManyField(to='posts.Categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
            ],
            options={
                'verbose_name': 'Artigo',
                'verbose_name_plural': 'Artigos',
            },
        ),
    ]
