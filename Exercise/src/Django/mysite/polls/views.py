from django.shortcuts import render
# Create your views here.

def index(request):
	return render(request,'poll.html',{})

def start(request):
	return render(request,'start.html',{})
