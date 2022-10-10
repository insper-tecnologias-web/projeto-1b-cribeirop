from django.shortcuts import render, redirect
from .models import Note
from database import Database

db = Database('notes')

def index(request):
    if request.method == 'POST':
        if request.POST.get("verb") == "add":
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            note = Note(title=title, content=content)
            note.save()
            return redirect('index')

        elif request.POST.get("verb") == "delete":
            title = request.POST.get('titulo')
            for note in Note.objects.all():
                if note.title == title:
                    note.delete()
                    return redirect('index')  

        # elif request.POST.get("verb") == "update":
        #     id = request.POST.get('id')
        #     for note in Note.objects.all():
        #         if note.id == id:
        #             note = Note(title=request.POST.get('titulo'), content=request.POST.get('detalhes'))
        #             note.save()
        #             return redirect('index')  
            
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request,id):
    if request.method == 'POST':
        id = request.POST.get('id')
        note = Note.objects.filter(id=id)
        note.update(title=request.POST.get('titulo'), content=request.POST.get('detalhes'))
        # for note in Note.objects.all():
        #     if note.id == id:
        # title = request.POST.get('titulo')
        # content = request.POST.get('detalhes')
        # note = Note(title=title, content=content)
        # note.save()
        return redirect('index')  
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/edit.html', {'notes': all_notes})