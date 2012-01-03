from django import template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('posts/post_modal.html')
def post_modal(post):
    c = {'post': post}
    c['photos'] = []
    photos = post.photos.all()
    for i, photo in enumerate(photos):
        prev = photos[i - 1] if i > 0 else ''
        nxt = photos[i + 1] if i + 1 < len(photos) else ''
        c['photos'].append((prev, i + 1, nxt, photo))
    return c

@register.inclusion_tag('posts/breadcrumbs.html')
def breadcrumbs(post=None):
    links = [("Home", reverse("zoe.posts.views.post_list"))]
    if post is not None:
        links.append((post, reverse("zoe.posts.views.post_detail",
                                    kwargs={'slug': post.slug})))
    return {'links': links}
