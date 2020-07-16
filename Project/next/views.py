from django.shortcuts import render

# Create your views here.
def next(request):
	context = {
	'title':'What Next',
	'judul':'NEXT',
	'Subjudul':'What Next Learning',
	'link':[
		['/home', 'HOME'],
		['/', 'BACK'],
	],
	'content_1':'Model And Database',
	'content_2':'Stay Tune',
	}

	return render(request, 'next.html', context)