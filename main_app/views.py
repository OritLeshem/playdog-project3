from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Dog, Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class DogCreate(CreateView):
  model = Dog
  fields = ['name','breed', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the cat
    return super().form_valid(form)
  # success_url = '/dogs/'
class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

def DeleteDog(request, pk):
  dog=Dog.objects.get(id=pk)
  dog.delete()
  return redirect('dogs_index')
 
def home(request):
    return render(request, 'home.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  # events_dog_dosnt_have=Event.objects.exclude(id__in = dog.events.all().values_list('id'))
  # events=Event.objects.all()
  return render(request, 'dogs/detail.html', { 'dog': dog})  

