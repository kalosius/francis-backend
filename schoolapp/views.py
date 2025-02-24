from django.shortcuts import render
from .forms import SeniorOneForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SeniorOneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'success.html')
    else:
        form = SeniorOneForm()
    return render(request, 'index.html', {'form': form})