from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formpage(request):

    context = {
        'title': 'Handouts',
        'date': 1920
    }

    return render(request, 'home.html', context=context)