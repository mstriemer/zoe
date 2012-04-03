from django import template
from django.utils.safestring import mark_safe
from django.utils import simplejson as json
from django.core.urlresolvers import reverse

from sorl.thumbnail import get_thumbnail

from zoe.posts.models import Post

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

@register.simple_tag
def to_json(posts):
    if isinstance(posts, Post):
        posts = [posts]
    return json.dumps([_serialize_post(post) for post in posts])

def _serialize_post(post):
    return {
        'id': post.pk,
        'title': post.title,
        'content': post.content,
        'photos': [_serialize_photo(photo) for photo in post.photos.all()]
    }

def _serialize_photo(photo):
    thumbnail = get_thumbnail(photo.image, '520x360')
    return {
        'id': photo.pk,
        'caption': photo.caption,
        'full_url': photo.image.url,
        'url': thumbnail.url,
        'height': thumbnail.height,
        'width': thumbnail.width
    }
