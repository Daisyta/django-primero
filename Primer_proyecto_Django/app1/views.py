
# Create your views here.
from django.shortcuts import redirect, render, HttpResponse


def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('<h1>Placeholder para luego mostrar una lista de todos los blogs</h1>')

def new(request):
    return HttpResponse('<h1>Placeholder para mostrar un nuevo formulario para crear un nuevo blog</h1>')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"<h1>Placeholder para mostrar el blog numero: {number}</h1>")

def edit(request, number):
    return HttpResponse(f"<h1>Placeholder para editar el blog {number}</h1>")

def destroy(request, number):
    return redirect('/blogs')