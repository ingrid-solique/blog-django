from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, verbose_name='sub-titulo', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True)
    conteudo = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='autor')
    categorias = models.ManyToManyField(Categoria, verbose_name='Catgeorias')

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    nomeUsuario = models.CharField(max_length=255, null=True, blank=True, verbose_name='nome')
    conteudo = models.TextField(verbose_name='comentario')
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return  self.nomeUsuario
