from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird, Gift
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds': birds })

def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    unassigned_gifts = Gift.objects.exclude(id__in = bird.gifts.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {
        'bird': bird, 
        'feeding_form': feeding_form,
        'gifts': unassigned_gifts
    })

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('detail', bird_id=bird_id)

def assoc_gift(request, bird_id, gift_id):
    Bird.objects.get(id=bird_id).gifts.add(gift_id)
    return redirect('detail', bird_id=bird_id)

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'colors', 'count']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'