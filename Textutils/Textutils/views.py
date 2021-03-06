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
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capfirst=request.POST.get('capfirst','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')


    if removepunc=="on":
        Punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in Punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}

        #return render(request,'analyze.html',params)
        djtext=analyzed


    if(capfirst=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        
        
        params={'purpose':'Changed to Upper Case','analyzed_text':analyzed}

        # return render(request,'analyze.html',params)
        djtext=analyzed

    
    if(newlineremover == "on"):
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    
    if(extraspaceremover == "on"):
        analyzed = ''
        for i in range(len(djtext)):
            if djtext[i]== ' ' and djtext[i+1]== ' ':
                pass
            else:
                analyzed=analyzed+djtext[i]

        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
        djtext=analyzed

    if (charcount=='on'):
        count=0
        for char in djtext:
            if char != ' ':
                count=count+1


        params = {'purpose': 'Character Count', 'analyzed_text': count}
        # Analyze the text
        #djtext=analyzed

    if(removepunc!='on' and newlineremover!='on' and capfirst!='on' and extraspaceremover!='on' and charcount !='on' ):
        return HttpResponse("Error! Please Select any operation or give text ")
    
    return render(request, 'analyze.html', params)


    





    #analyzed=djtext
    
    #print(djtext)
    #print(analyze)
    

# def capfirst(request):
#     return HttpResponse(''' <h2>Capitalize</h2> <a href='https://github.com/kpkrishan?tab=repositories'>My Github</a>  <a href='/'> Back</a>''')

# def newline(request):
#     return HttpResponse('''<h3>add newline</h3> <a href='/'> Back</a>''')

# def spaceremover(request):
#     return HttpResponse(''' 'It removes the space' <a href='https://www.youtube.com/watch?v=0dBZZOYIDW0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=9'> Django tutorial</a> <a href='/'> Back</a>''')

# def charcount(request):
#     return HttpResponse('''<h1>counting the character!</h1> <a href='/'> Back</a>''')


def Contact_Us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')