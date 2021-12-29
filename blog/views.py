from django.shortcuts import render

from .models import Article

def blog(request):
    posts = Article.objects.order_by('published_date').filter(is_published=True)

    context = {
        'posts' : posts
    }

    return render(request, 'blog/blog.html', context)
