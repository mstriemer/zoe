from django.shortcuts import get_object_or_404, render_to_response

from posts.models import Post

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('posts/post_detail.html', {'post': post})
