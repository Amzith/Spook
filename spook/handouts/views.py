from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import HandoutForm

# Create your views here.
def formpage(request):

    # Handle Form 
    if request.method == "POST":
        form = HandoutForm(request.POST)

        if form.is_valid():
            output_text = form.cleaned_data["contents_text"]
            return render(request, 'output.html', {"output_text":output_text})
    
    else:
        form = HandoutForm()

    context = {
        'title': 'Handouts',
        'date': 1920,
        "form": form
    }

    return render(request, 'home.html', context=context)

