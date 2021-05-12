from django.shortcuts import render

def personalsite(request):
	personal_info = {'name': 'Deyan Chen',
					 'phone_num': '+(86) 155-210-44810',
					 'email': 'deyanchen89@gmail.com',
					 'address': 'California'}
	return render(request, 'index.html', personal_info)