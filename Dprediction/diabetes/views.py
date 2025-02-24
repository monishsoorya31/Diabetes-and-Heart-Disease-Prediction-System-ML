from django.shortcuts import render
from .models import persons


def diabetes(request):

    person  =  persons.objects.all()

    return render(request, 'index.html', { 'person' : person})



