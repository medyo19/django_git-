from operator import index
from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies'{
         'id':1
         'title':'The office'
    '     year':1996 # type: ignore
             }
           {
          'id':1
          'title':'The office'
           'year':1996 # type: ignore
            }
           {
            'id':1
            'title':'The office'
            'year':1996 # type: ignore
             }
          }

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def order(request):
    return render(request,'movies/index.html',data)
