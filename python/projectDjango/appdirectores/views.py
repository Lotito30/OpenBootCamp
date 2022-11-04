from django.shortcuts import render
from .models import Director
from django.db.models import Q 

def index(request):
    query = request.GET.get('pregunta','')
    if query:
        qset = (
            Q(Name__icontains=query)|
            Q(Last_Name__icontains=query)
        )
        director = Director.objects.filter(qset)

    else:
        director = Director.objects.filter(Name='')
    return render(
        request,
        'appdirectores/index.html',
        {'director':director,
        'query':query,
        }
    )
