from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

# Create your views here.
def list (request):
    lista_de_notas = Note.objects.order_by("creation_date_note")

    context = {
        "lista_de_notas": lista_de_notas,
    }

    return render(request, "notes_UrielRonaldoMendozaNuñez/list_MendozaNuñez.html", context)

def detail (request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    return render(request, "notes_UrielRonaldoMendozaNuñez/detail_MendozaNuñez.html", {"note":note})

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:list')  # Redirige a la vista que muestra todas las notas
    else:
        form = NoteForm()
    
    return render(request, 'notes_UrielRonaldoMendozaNuñez/edit_MendozaNuñez.html', {'form': form})



def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:list')  # Redirige a la lista de notas después de guardar
    else:
        form = NoteForm(instance=note)  # Carga la instancia de la nota en el formulario

    return render(request, 'notes_UrielRonaldoMendozaNuñez/edit_MendozaNuñez.html', {'form': form, 'note': note})


def delete(request, note_id):
    # Obtiene la nota por su ID o muestra un error 404 si no se encuentra
    note = get_object_or_404(Note, pk=note_id)

    # Si la solicitud es POST, elimina la nota
    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')  # Redirige a la lista de notas

    # Si no es una solicitud POST, muestra una confirmación de eliminación
    return render(request, 'notes_UrielRonaldoMendozaNuñez/edit_MendozaNuñez.html', {'note': note})





