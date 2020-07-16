from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
	'judul':'HOME',
	'Subjudul':'WELCOME HOME',
	'link':[
		['/home/next', 'NEXT'],
		['/', 'BACK'],
		],
	'image':'home/img/home.png',
	}
	return render(request, 'home/home.html', context)

def next(request):
	context = {
	'judul':'NEXT',
	'Subjudul':'WELCOME NEXT',
	'link':[
		['/home', 'HOME'],
		['/', 'BACK'],
	],
	'image':'home/img/next.png',
	}
	return render(request, 'home/home.html', context)