from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('', views.hello_name, name="hello_name"),
    path('html', views.hello_html, name="hello_html")
]


