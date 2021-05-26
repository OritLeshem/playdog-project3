from django.shortcuts import render, redirect
from .models import Dog, Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def testmap(request):
    return render(request, 'map.html')


def home(request):
    return render(request, 'home.html')

# DOGS:_________________


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    # events_dog_dosnt_have=Event.objects.exclude(id__in = dog.events.all().values_list('id'))
    # events=Event.objects.all()
    return render(request, 'dogs/detail.html', {'dog': dog})


class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age', 'size', 'gender', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age', 'size', 'gender']


@login_required
def DeleteDog(request, pk):
    dog = Dog.objects.get(id=pk)
    dog.delete()
    return redirect('dogs_index')


# EVENTS:_________________
class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'description', 'date', 'location', 'lat', 'lng', 'time']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/events/'


def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/events_index.html', {'events': events})

def events_map(request):

    events = Event.objects.all()
    lats = []
    lngs = []
    for event in events:
            lats.append(event.lat)
            lngs.append(event.lng)

    return render(request, 'events/events_map.html',{'lats' : [float(i) for i in lats], 'lngs' : [float(i) for i in lngs]})


@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    my_dogs = Dog.objects.filter(user=request.user)
    dogs_not_attending = my_dogs.exclude(
        id__in=event.attendees.all().values_list('id'))
    return render(request, 'events/events_detail.html', {
        'event': event,
        'my_dogs': my_dogs,
        'dogs_not_attending': dogs_not_attending
    })


class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'description', 'date', 'location', 'lat', 'lng', 'time']
    success_url = '/events/'


def DeleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('events_index')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('dogs_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def assoc_dog(request, event_id, dog_id):
    Event.objects.get(id=event_id).attendees.add(dog_id)
    return redirect('events_detail', event_id=event_id)


@login_required
def unassoc_dog(request, event_id, dog_id):
    Event.objects.get(id=event_id).attendees.remove(dog_id)
    return redirect('events_detail', event_id=event_id)
