from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):

    return render(request,'core/home.html')


def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            #auntenticar al usuario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
             


    return render(request, 'registration/registro.html', data)