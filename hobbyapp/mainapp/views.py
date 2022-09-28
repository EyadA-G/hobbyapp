from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from rest_framework import serializers
from django.core import serializers as core_serializers
from json import dumps
from mainapp.models import Users, Hobbies
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required

from mainapp.serializer import UserSerializer
def view_all(request):
    name = get_user_model()
    username = request.user
    all = Users.objects.all()
    usern = Users.objects.get(user=username)
    hobbies = Hobbies.objects.all()
    data = (UserSerializer(all, many=True, context={'request': request}).data)
    hobby = Hobbies.objects.filter(userHobbies = usern)
    user = Users.objects.filter(user = username)


    context = {
        'username': username,
        'usern': usern,
        'name': name,
        'hobbies': hobbies,
        'data': data,
        'hobby': hobby,
        'user': user

                }
    
    return render(request, 'main/users.html', context)

def loginPage(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        admin = authenticate(request, username="admin", password=password)
        if admin is not None:
            login(request, admin)
            return redirect('admin')
        elif user is not None:
            login(request, user)
            return redirect('users')
        else:
            messages.success(request, 'Username or Password is incorrect.')                                           
    context = {}        
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def filter_hobbies(request):
    userIs = request.user
    qs = Users.objects.all()
    hobby = Hobbies.objects.all()
    username = Users.objects.all()
    context = {
        'hobbies': hobby,
        'username': username,
        'user': userIs,
        'queryset': qs,
                }
    return render (request, 'main/hobbies.html', context)