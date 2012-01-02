"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime

from django.test import TestCase
from django.test.client import Client

from posts.models import Post, Photo


class PostTest(TestCase):
    def test_unicode(self):
        assert u'My Post' == unicode(Post(title='My Post'))

    def test_date_created(self):
        now = datetime.now()
        post = self.make_post()
        assert now < post.date_created

    def test_date_updated(self):
        post = self.make_post()
        initial = post.date_updated
        post.save()
        assert initial < post.date_updated

    def make_post(title='Post', slug='post', **kwargs):
        return Post.objects.create(title=title, slug=slug, **kwargs)

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_detail(self):
        post = self.make_post()
        response = self.client.get('/posts/post/')
        assert post == response.context['post']
        assert 200 == response.status_code
        assert 'posts/post_detail.html' == response.templates[0].name

    def make_post(self, title='Post', slug='post', **kwargs):
        return Post.objects.create(title=title, slug=slug, **kwargs)


class PhotoTest(TestCase):
    fixtures = ['posts.json', 'photos.json']

    def test_photo(self):
        # photo = Photo.objects.get(pk=1)
        pass
