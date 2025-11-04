from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem

# Create your views here.
def index (request):
    return render(request, 'supermegaultraindex.html')


def toDoAppView (request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'home.html', {'all_items': all_todo_items})

def newadd (request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteitem (request, it):
    y = TodoListItem.objects.get(id=it)
    y.delete()
    return HttpResponseRedirect('/todoapp/')
