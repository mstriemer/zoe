from django.views.generic import ListView, DetailView

from posts.models import Post

post_detail = DetailView.as_view(
        model=Post,
        template_name='posts/post_detail.html',
        context_object_name='post')

post_list = ListView.as_view(
        model=Post,
        template_name='posts/post_list.html',
        paginate_by=5,
        queryset=Post.objects.published(),
        context_object_name='posts')
