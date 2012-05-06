from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.models import Post

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.published(), slug=slug)
    return render_to_response('posts/post_detail.html', {'post': post})

def post_list(request):
    post_list = Post.objects.published()
    pages = Paginator(post_list, 5)
    try:
        page = pages.page(request.GET.get('page', 1))
    except PageNotAnInteger:
        page = pages.page(1)
    except EmptyPage:
        page = pages.page(pages.num_pages)
    posts = page.object_list
    return render_to_response('posts/post_list.html', {'posts': posts,
        'page': page})
