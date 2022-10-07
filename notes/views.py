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
            db.add(Note(title,content))
            # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
            return redirect('index')
        elif request.POST.get("verb") == "delete":
            title = request.POST.get('titulo')
            for note in Note.objects.all():
                if note.title == title:
                    note.delete()
                    # db.delete(note.id)
                    break
            # id = request.POST.get('id')
            # for note in Note.objects.all():
            #     if id == note.id:
            #         note.delete()
            #         db.delete(note.id)
            #         break
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})