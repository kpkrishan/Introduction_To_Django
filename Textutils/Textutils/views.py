#Created By Krishan

from django.http import HttpResponse

#welcome 
def home(request):
    return HttpResponse("Hey! Krishan welcome to django!!")
#Pipeline in Django project
#textutil pipeline

def removepunc(request):
    return HttpResponse("Remove punctuation!")

def capfirst(request):
    return HttpResponse("Capitalize")

def newline(request):
    return HttpResponse("Add newline!")

def spaceremover(request):
    return HttpResponse("It removes the space")

def charcount(request):
    return HttpResponse("counting the character!")