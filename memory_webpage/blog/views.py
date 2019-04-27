from django.shortcuts import render

posts = [
    {
        'author': 'YZ',
        'title': 'First post',
        'content': 'R18'
    },
    {
        'author': 'YZ 2.0',
        'title': 'Second post',
        'content': 'content is hot'
    }
]

def home(request):
	context = {
	    'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'about about'})