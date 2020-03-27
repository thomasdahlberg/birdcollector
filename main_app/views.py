from django.shortcuts import render

birds = 1

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    return render(request, 'birds/index.html', { 'birds': birds })