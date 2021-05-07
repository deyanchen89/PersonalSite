from django.shortcuts import render

def personalsite(request):
	name = '陈德彦'
	return render(request, 'index.html', {'name': name})