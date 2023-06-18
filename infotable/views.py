from django.shortcuts import render
from .models import Person

# Create your views here.
def infoTableView(request):
    data = Person.objects.all()

    context = {
        "missing_persons" : data
    }

    return render(request, "infotable/table.html", context)

def individualPersonView(request, personID):
    data = Person.objects.filter(
        id = personID
    ).get()

    context = {
        "person" : data
    }

    return render(request, "infotable/person.html", context)
