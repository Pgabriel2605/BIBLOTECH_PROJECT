from django.contrib import admin
from .models import Genero, Editora, Autor, Livro

# Register your models here.
admin.site.Register(Genero)
admin.site.Register(Editora)
admin.site.Register(Autor)
admin.site.Register(Livro)
