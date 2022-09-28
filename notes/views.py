from django.shortcuts import render, redirect
from .models import Note
from database import Database

db = Database('notes')

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title=title, content=content)
        note.save()
        db.add(Note(title,content))
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})