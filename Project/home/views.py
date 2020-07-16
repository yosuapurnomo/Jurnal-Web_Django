from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
	'title':'HOME',
	'judul':'HOME',
	'Subjudul':'WELCOME HOME',
	'link':[
		['/home/next', 'NEXT'],
		['/', 'BACK'],
		],
	'content_1':'Surabaya, Indonesia',
	'content_2':'Jl. Jogoloyo 3 No.3',
	}
	return render(request, 'home/home.html', context)