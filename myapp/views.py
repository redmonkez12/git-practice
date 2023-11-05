from django.shortcuts import render

from myapp.forms import TodosForm
from myapp.models import Todo


# Create your views here.
def index(request):
    context = {"form": TodosForm, "todos": Todo.objects.all()}
    return render(request, "index.html", context)


def create_todo(request):
    if request.method == "POST":
        form = TodosForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return render(request, "todo_partial.html", {"todo": todo})

    return render(request, "todo_form.html", {"form": TodosForm})
