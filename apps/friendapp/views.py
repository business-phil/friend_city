from django.shortcuts import render, redirect
from .models import Person, Friendship

def index(request):
    friendship_query = Friendship.objects.all()
    people_query = Person.objects.all()
    context = { 'friendships': friendship_query, 'friends': people_query }
    return render(request, 'friendapp/index.html', context)

def create(request):
    Person.objects.create(name=request.POST['name'])
    return redirect('/')

def friendify(request):
    person = Person.objects.get(id=request.POST['person'])
    friend = Person.objects.get(id=request.POST['friend'])
    Friendship.objects.create(person=person, friend=friend)
    return redirect('/')
