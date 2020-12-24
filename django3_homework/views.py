from django.shortcuts import render


def index(request):
    context={
        'hello':'hello world'
    }
    return render(request,'index.html',context)