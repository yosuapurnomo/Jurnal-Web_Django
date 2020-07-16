from django.shortcuts import render

def welcome(request):
	context = {
	'title':'WELCOME',
	'judul':'JURNAL YOSUA',
	'image':'img/welcome.jpg',
	'Subjudul':'Website ini dibuat dengan Django',
	'link':[
	['/home','HOME'],
	['/admin','ADMIN'],
	],
	'content_1':'Yosua Purnomo',
	'content_2':'Institut Teknologi Adhi Tama Surabaya',
	}
	return render(request, 'welcome.html', context)