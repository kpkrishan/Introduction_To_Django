#Created By Krishan

from django.http import HttpResponse

#welcome 
def home(request):
    return HttpResponse("Hey! Krishan welcome to django!!")
#Pipeline in Django project
#textutil pipeline

def removepunc(request):
    return HttpResponse('''<h1>Remove punctuation!</h1>  <a href='/'> Back</a>''')

def capfirst(request):
    return HttpResponse(''' <h2>Capitalize</h2> <a href='https://github.com/kpkrishan?tab=repositories'>My Github</a>  <a href='/'> Back</a>''')

def newline(request):
    return HttpResponse('''<h3>add newline</h3> <a href='/'> Back</a>''')

def spaceremover(request):
    return HttpResponse(''' 'It removes the space' <a href='https://www.youtube.com/watch?v=0dBZZOYIDW0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=9'> Django tutorial</a> <a href='/'> Back</a>''')

def charcount(request):
    return HttpResponse('''<h1>counting the character!</h1> <a href='/'> Back</a>''')