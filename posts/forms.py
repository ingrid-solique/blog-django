from django.forms import ModelForm
from django import forms
from .models import Comentario


class FormComentario(ModelForm):
    class Meta:
        model = Comentario
        fields = ['nomeUsuario', 'conteudo']
