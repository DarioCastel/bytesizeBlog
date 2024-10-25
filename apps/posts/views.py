from django.shortcuts import render, redirect
from .models import Posts, User, Comentarios, Categorias, Contacto
from .form import (
    RegistroForm,
    ModificarForm,
    ModificarComentarioForm,
    CustomLoginForm,
    ContactForm,
)
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages

# vista basada en funciones
# def posts(request):
#     ctx = {}  # contextos
#     noticias = Posts.objects.all().order_by("-id")  # select * from Posts
#     ctx["noticias"] = noticias

#     return render(request, "posts/posts.html", ctx)


class Noticias(ListView):
    model = Posts
    template_name = "posts/posts.html"
    # paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        # print(queryset)
        # fecha
        ordenar_por = self.request.GET.get("ordenar")
        direccion = self.request.GET.get("direccion")
        print(ordenar_por)
        if ordenar_por == "fecha":
            if direccion == "asc":
                queryset = queryset.order_by("fecha_publicacion")  # Ascendente
            elif direccion == "desc":
                queryset = queryset.order_by("-fecha_publicacion")  # Descendente
        elif ordenar_por == "alfabetico":
            if direccion == "asc":
                queryset = queryset.order_by("titulo")  # A-Z
            elif direccion == "desc":
                queryset = queryset.order_by("-titulo")  # Z-A


        # por autor
        autor = self.request.GET.get("autor")
        if autor:
            queryset = queryset.filter(autor__username=autor)

        # por categorias
        categoria = self.request.GET.get("categoria")
        if categoria:
            queryset = queryset.filter(categoria__nombre=categoria)

        # print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categorias.objects.all()
        return context



def post_id(request, id):
    ctx = {}
    noticia = Posts.objects.get(id=id)
    comentarios = Comentarios.objects.filter(post=noticia)
    ctx["noticia"] = noticia
    ctx["comentarios"] = comentarios
    return render(request, "posts/detalle.html", ctx)


def about_us(request):
    return render(request, "posts/about_us.html")


def perfil(request, id):
    ctx = {}
    usuarios = User.objects.get(id=id)
    ctx["usuarios"] = usuarios
    print(usuarios)
    return render(request, "usuarios/perfil.html", ctx)


# vista basada en clase
class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("login")
    template_name = "usuarios/registro.html"


# views login
class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm


class CrearPost(CreateView):
    form_class = ModificarForm
    model = Posts
    template_name = "posts/crear_post.html"
    success_url = reverse_lazy("noticias")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EliminarPost(DeleteView):
    model = Posts
    success_url = reverse_lazy("noticias")


class ModificarPost(UpdateView):
    model = Posts
    form_class = ModificarForm
    template_name = "posts/modificar_post.html"
    success_url = reverse_lazy("noticias")


@login_required
def comentar_post(request):
    comentario = request.POST.get("comentario", None)
    user = request.user
    post = request.POST.get("id_noticia", None)
    get_post = Posts.objects.get(pk=post)
    coment = Comentarios.objects.create(autor=user, contenido=comentario, post=get_post)

    return redirect(reverse_lazy("detalle", kwargs={"id": post}))


class ModificarComentario(UpdateView):
    model = Comentarios
    form_class = ModificarComentarioForm
    template_name = "comentarios/modificar.html"
    success_url = reverse_lazy("noticias")


class EliminarComentario(DeleteView):
    model = Comentarios
    template_name = "comentarios/confirm_delete.html"
    success_url = reverse_lazy("noticias")


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar los datos en la base de datos
            Contacto.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['mensaje']
            )
            return redirect('contacto')  # Redirigir después de guardar
    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form})