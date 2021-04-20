from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import NoteForm
from .models import Note


def add(request, id=-1):
    template_name = 'enroll/add.html'
    
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    

    notes = Note.objects.all()
    context = {
        'notes':tuple(zip(notes, [i for i in range(1, len(notes)+1)])),
        'form': form,
    }
    return render(request, template_name, context)


def update(request, id):

    if request.method == 'POST':
        note = Note.objects.get(pk=id)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note.save()
            return redirect('add')
    try:
        note = Note.objects.get(pk=id)
        form = NoteForm(instance=note)

        context = {
            'note': note,
            'form': form,
        }
        return render(request, 'enroll/update.html', context)
    except ObjectDoesNotExist:
        return redirect('add')


def delete(request, id):
    try:
        note = Note.objects.get(pk=id)
        note.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('add')