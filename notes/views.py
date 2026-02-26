# from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
def set_cookie_data(request):
    response = HttpResponse("Setting cookie from server")
    response.set_cookie('user',"bibek ghimire", max_age = 86400*30)
    return response
def index(request):
    notes = Note.objects.all().order_by('-id')
    return render(request,"notes/index.html",{'notes':notes})

def add_note(request):
    if request.method =='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.create(form.cleaned_data)
            messages.success(request, 'Data added successfully')

            return redirect('notes:index')
    else:
        form = NoteForm()
    return render(request,"notes/add.html",{
        "form":form
    })
@csrf_exempt  
def add_note_sql_injection(request):
    if request.method =='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['description']
            sql = f"""
            INSERT INTO notes_note (title,description)
            VALUES ('{title}','{desc}');
            """

            with connection.cursor() as cursor:
                cursor.executescript(sql)

            messages.success(request, 'Data added successfully')

            return redirect('notes:index')
    else:
        form = NoteForm()
    return render(request,"notes/add.html",{
        "form":form
    })
def delete_note(request,note_id):
    note = get_object_or_404(Note,id=note_id)
    note.delete()
    messages.success(request,"note deleted successfully")
    return redirect('notes:index')
