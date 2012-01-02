from django import template
from django.utils.safestring import mark_safe

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
