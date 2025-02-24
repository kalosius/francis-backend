from django.shortcuts import render
from .forms import SeniorOneForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SeniorOneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SeniorOneForm()
    return render(request, 'index.html', {'form': form})