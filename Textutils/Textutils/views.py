#Created By Krishan

from django.http import HttpResponse

#welcome 
def home(request):
    return HttpResponse("Hey! Krishan welcome to django!!")
#Pipeline in Django project
#textutil pipeline

def removepunc(request):
    return HttpResponse("<h1>Remove punctuation!</h1>")

def capfirst(request):
    return HttpResponse("<h2>Capitalize</h2>")

def newline(request):
    return HttpResponse("add newline")

def spaceremover(request):
    return HttpResponse("It removes the space")

def charcount(request):
    return HttpResponse("counting the character!")