from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('', views.hello_name, name="hello_name"),
    path('html', views.hello_html, name="hello_html"),
    path('special', views.special_view, name="special_view"),
    path('helloquery', views.hello_query, name="hello_query"),
    path('helloname/<str:name>', views.hello_path, name="hello_name"),
    path('postendpoint', views.post_example, name="post"),
    path('submitendpoint', views.submit, name="submit"),
    path('profile/<str:name>/<int:age>', views.profile, name="profile"),
]


