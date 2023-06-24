from django.shortcuts import render, redirect, get_object_or_404

from .models import Note
from .forms import TaskForm, UserRegistration


# Create your views here.

# app landing page
def index(request):
    return render(request, 'index/index.html')

# notes landing page
def notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'index/notes.html', {
        'notes': notes
    })

# create note view
def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes')
    else:
        form = TaskForm

    return render(request, 'index/add.html', {
        'form': form
    })

# update note view
def edit(request, note_id):
    note = get_object_or_404(Note, id = note_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = note)
        if form.is_valid():
            form.save()
            return redirect('notes')
        
    else:
        form = TaskForm(instance = note)

    return render(request, 'index/edit.html', {
        'form' : form,
        'note' : note
    })

# delete note view
def delete(request, note_id):
    note = get_object_or_404(Note, id = note_id)

    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    
    return render(request, 'index/delete.html', {
        'note' : note
    })

# User registartion view
def createUser(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
        
    else:
        form = UserRegistration
    
    return render(request, 'index/createUser.html', {
        'form' : form
    })