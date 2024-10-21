from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Note

# Create your views here.
def list (request):
    lista_de_notas = Note.objects.order_by("creation_date_note")

    context = {
        "lista_de_notas": lista_de_notas,
    }

    return render(request, "notes_UrielRonaldoMendozaNuñez\list_MendozaNuñez.html", context)

def detail (request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    return render(request, "notes_UrielRonaldoMendozaNuñez/detail_MendozaNuñez.html", {"note":note})

def create (request,):
    return

def edit (request,):
    return

def delete (request,):
    return





