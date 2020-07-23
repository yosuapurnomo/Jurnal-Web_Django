from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):

	posts = Post.objects.all()[0]
	print(posts)
	context = {
	'title':'HOME',
	'judul':'HOME',
	'Subjudul':'WELCOME HOME',
	'link':[
		['/next', 'NEXT'],
		['/', 'BACK'],
		],
	'contain1':posts.title,
	'contain2':posts.body,
	}
	return render(request, 'home/home.html', context)