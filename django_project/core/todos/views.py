from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def hello_world_view(request):
    return HttpResponse('Hello World!')

def hello_name(request):
    return HttpResponse("Parth Chauhan")

def hello_html(request):
    return render(request, 'todos/hello.html')

def hello_path(request, name):
    return HttpResponse(f'Hello, {name}')

def hello_query(request):
    return HttpResponse(f'your query was {request.GET.get("q")}')

def special_view(request):
    return redirect('hello_html')

