from django.contrib import admin
from posts.models import Post, Categoria, Comentario

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('categorias', )

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)
admin.site.register(Comentario)
