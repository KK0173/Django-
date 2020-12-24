from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
     return redirect(reverse('user:denglu'))

def game(request):
     return  render(request,'index.html')