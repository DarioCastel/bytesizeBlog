from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Posts, Comentarios


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        max_length=200,
        label="Nombre de Usuario", 
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"},
        ),
    )
    email = forms.EmailField(
        max_length=200,
        help_text="Obligatorio",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "name@example.com"}
        ),
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}), required=True
    )
    password2 = forms.CharField(
        label="Repetir la contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}), required=True
    )
    icono = forms.ImageField(
        label="Imagen de perfil",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "icono",
        ]
        # widget = {
        #     "username": forms.Textarea(attrs={"class": "form-control"}),
        #     "email": forms.EmailField(attrs={"class": "form-control"}),
        #     "password1": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "icono": forms.ImageField(attrs={"class": "form-control"}),
        # }


class CrearForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ("contenido",)
        fields = ['titulo', 'encabezado', 'contenido', 'categoria', 'imagen1', 'imagen2']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'encabezado': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        exclude = ["autor"]


class ModificarForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ("contenido",)
        fields = ['titulo', 'encabezado', 'contenido', 'categoria', 'imagen1', 'imagen2']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'encabezado': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# Formulario Comentarios


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = [
            "contenido",
        ]


class ModificarComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = [
            "contenido",
        ]

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"},
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Ingrese la contraseña"}
        ),
        required=True,
    )

    class Meta:
        model = User
        fileds = ["username", "password"]