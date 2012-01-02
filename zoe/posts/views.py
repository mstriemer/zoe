from django.shortcuts import get_object_or_404, render_to_response

from posts.models import Post

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('posts/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render_to_response('posts/post_list.html', {'posts': posts})
