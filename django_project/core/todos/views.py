from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

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

def profile(request, name, age):
    return HttpResponse(f'hello my name is {name}, i am {age} years old.')

def post_example(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age  = request.POST.get('age')

        return HttpResponse(f'you posted: {name}, {age}')
    else:
        return HttpResponseNotAllowed('POSt')

def submit(request):
    return render(request, 'todos/submit.html')

