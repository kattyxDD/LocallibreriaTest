from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    """
    Funcion vista para la pagina del sitio
    """
    #genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    #libros disponibles (status ='a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  #el 'all()' esta implicito por defecto

    #renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,
        'num_instances_available':num_instances_available, 'num_authors':num_authors},
    )
