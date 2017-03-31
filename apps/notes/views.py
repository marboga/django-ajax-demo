from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note

# Create your views here.
def index(request):
    print 'in index'
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/index.html', context)

def create(request):
    print 'in create method'
    if request.method == 'POST':
        valid, res = Note.objects.validate(request.POST)
        if not valid:
            for error in res:
                messages.error(request, error)
        else:
            print 'new note created:', res

    return redirect('notes:partial')

def delete(request, id):
    print 'in delete method, id= ', id
    Note.objects.remove(id)
    context = { 'notes': Note.objects.all() }
    return render(request, 'notes/partial.html', context)

def partial(request):
    print "about to render partial"
    context = { 'notes': Note.objects.all() }
    return render(request, 'notes/partial.html', context)
