from django.shortcuts import get_object_or_404, render

from .models import Article

def blog(request):
    posts = Article.objects.order_by('published_date').filter(is_published=True)

    context = {
        'posts' : posts
    }

    return render(request, 'blog/blog.html', context)

def post(request, post_id):
    post = get_object_or_404(Article, pk=post_id)

    context = {
        'post' : post
    }

    return render(request, 'blog/post.html', context)
