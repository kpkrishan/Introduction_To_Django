#Created By Krishan

from django.http import HttpResponse
from django.shortcuts import render

#welcome 
def home(request):
    #detail={'Name':'Krishan','Place':'Kushinagar'}
    #detail is an variable and it can also be an argument for render.
    #we can access the value via key of detail.
    return render(request,'home.html')
    #return HttpResponse("Hey! Krishan welcome to django!!")
#Pipeline in Django project
#textutil pipeline

def removepunc(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    if removepunc=="on":
        Punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in Punctuations:
                analyzed=analyzed+char
    else:
        return HttpResponse(''' "Error!!" <a href='/Back>'>Go Back</a>''')
    #analyzed=djtext
    params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
    print(djtext)
    print(removepunc)
    return render(request,'removepunc.html',params)

# def capfirst(request):
#     return HttpResponse(''' <h2>Capitalize</h2> <a href='https://github.com/kpkrishan?tab=repositories'>My Github</a>  <a href='/'> Back</a>''')

# def newline(request):
#     return HttpResponse('''<h3>add newline</h3> <a href='/'> Back</a>''')

# def spaceremover(request):
#     return HttpResponse(''' 'It removes the space' <a href='https://www.youtube.com/watch?v=0dBZZOYIDW0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=9'> Django tutorial</a> <a href='/'> Back</a>''')

# def charcount(request):
#     return HttpResponse('''<h1>counting the character!</h1> <a href='/'> Back</a>''')