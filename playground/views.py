from django.shortcuts import render
# Create your views here.
# request handler

def hello_world(request):
    return render(request, 'hello.html', { 'name': "william" })