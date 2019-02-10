from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author":"Jannis",
        "title":"First blog post",
        "content":"This is the content of my first post",
        "date_posted":"10. Feburar 2019"
    },
    {
        "author":"Jana",
        "title":"Second blog post",
        "content":"This is the content of my second post",
        "date_posted":"08. Feburar 2019"
    }
]

def home(request):
    context = {
        "posts":posts,
        "title":'All posts'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')