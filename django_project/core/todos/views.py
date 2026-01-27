from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world_view(request):
    return HttpResponse('Hello World!')

def hello_name(request):
    return HttpResponse("Parth Chauhan")

def hello_html(request):
    return render(request, 'todos/hello.html')

