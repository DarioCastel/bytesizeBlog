from django.contrib import admin
from .models import Posts, Categorias, User, Contacto

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    search_fields = ("titulo",)
    list_filter = ["categoria", "autor__username"]
    list_display = ["titulo", "autor", "categoria"]
    date_hierarchy = "fecha_publicacion"


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email') 

admin.site.register(Contacto)
admin.site.register(Posts)
admin.site.register(Categorias)
admin.site.register(User)