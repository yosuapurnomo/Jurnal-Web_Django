from django.shortcuts import render

def welcome(request):
	context = {
	'judul':'JURNAL YOSUA',
	'image':'img/welcome.jpg',
	'Subjudul':'Website ini dibuat dengan Django',
	}
	return render(request, 'welcome.html', context)