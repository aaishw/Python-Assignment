from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    first_dict = {
        'read':"Hello I am coming from the Template Part within firstapp"

    }
    return render(request,'firstapp/index.html',context = first_dict)
    #return HttpResponse("Hello Welcome to Python")

#def index1(request):
 #   return HttpResponse("This is coming from index1")