from zipfile import ZipFile
import os
from datetime import datetime

from django.db import models
from django.conf import settings
from sorl.thumbnail import ImageField, get_thumbnail


class PublishedPostManager(models.Manager):
    def get_query_set(self):
        return super(PublishedPostManager, self).get_query_set().exclude(
                date_published=None).order_by('-date_published', 'id')


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, editable=False)
    date_published = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(editable=False)

    objects = models.Manager()
    published = PublishedPostManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.date_updated = datetime.now()
        super(Post, self).save(*args, **kwargs)
        self._create_archive()

    @property
    def archive_path(self):
        return '{0}posts/archive/{1}.zip'.format(settings.MEDIA_ROOT, self.slug)

    @property
    def archive_url(self):
        return '{0}posts/archive/{1}.zip'.format(settings.MEDIA_URL, self.slug)

    @property
    def archive_size(self):
        if os.path.exists(self.archive_path):
            return os.stat(self.archive_path).st_size
        else:
            return None

    def _create_archive(self):
        with ZipFile(self.archive_path, 'w') as postzip:
            for photo in self.photos.all():
                postzip.write(photo.image.path, os.path.basename(photo.image.name))


class Photo(models.Model):
    image = ImageField(upload_to='photos')
    caption = models.CharField(max_length=255)
    post = models.ForeignKey('Post', related_name='photos')
    date_created = models.DateTimeField(default=datetime.now, editable=False)
    date_updated = models.DateTimeField(editable=False)

    def __unicode__(self):
        return self.caption

    def save(self, *args, **kwargs):
        self.date_updated = datetime.now()
        super(Photo, self).save(*args, **kwargs)
        for size in ('x150', '520x360'):
            get_thumbnail(self.image, size)
