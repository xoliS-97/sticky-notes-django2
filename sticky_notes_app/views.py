from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'sticky_notes_app/home.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'sticky_notes_app/add_note.html', {'form': form})

from django.shortcuts import get_object_or_404

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'sticky_notes_app/edit_note.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')
