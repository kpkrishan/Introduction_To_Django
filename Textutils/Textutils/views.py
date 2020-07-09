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

def analyze(request):
    djtext=request.GET.get('text','default')
    analyze=request.GET.get('analyze','off')
    capfirst=request.GET.get('capfirst','off')
    if analyze=="on":
        Punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in Punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(capfirst=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        
        params={'purpose':'Changed to Upper Case','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error!!")
    #analyzed=djtext
    
    print(djtext)
    print(analyze)
    

# def capfirst(request):
#     return HttpResponse(''' <h2>Capitalize</h2> <a href='https://github.com/kpkrishan?tab=repositories'>My Github</a>  <a href='/'> Back</a>''')

# def newline(request):
#     return HttpResponse('''<h3>add newline</h3> <a href='/'> Back</a>''')

# def spaceremover(request):
#     return HttpResponse(''' 'It removes the space' <a href='https://www.youtube.com/watch?v=0dBZZOYIDW0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=9'> Django tutorial</a> <a href='/'> Back</a>''')

# def charcount(request):
#     return HttpResponse('''<h1>counting the character!</h1> <a href='/'> Back</a>''')