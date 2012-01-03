from django.shortcuts import get_object_or_404, render_to_response

from posts.models import Post

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.published.all()
    return render_to_response('posts/post_detail.html', {'post': post, 'posts': posts})

def post_list(request):
    posts = Post.published.all()
    return render_to_response('posts/post_list.html', {'posts': posts})
