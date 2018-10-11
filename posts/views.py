from django.shortcuts import render, redirect
from posts.models import Post, Categoria, Comentario
from posts.forms import FormComentario

# Create your views here.
def post_list(request):
    if 'categoria_id' in request.GET:
        posts = Post.objects.filter(categorias=request.GET['categoria_id'])
    else:
        posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'post_list.html', {
        'posts': posts,
        'categorias': categorias
    })


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    categorias = Categoria.objects.all()
    form = FormComentario(request.POST or None)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.post = post
        comentario.save()
        return redirect("post_show", post_id)
    comentarios = Comentario.objects.filter(post__id=post_id)

    return render(request, 'post_show.html', {
        'post': post,
        'categorias': categorias,
        'comentarios': comentarios,
        'form': form
    })
