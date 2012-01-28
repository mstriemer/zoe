from datetime import datetime
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from tasks import process_images


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


class Photo(models.Model):
    image = ImageField(upload_to='photos')
    caption = models.CharField(max_length=255)
    post = models.ForeignKey('Post', related_name='photos')
    date_created = models.DateTimeField(default=datetime.now, editable=False)
    date_updated = models.DateTimeField(editable=False)

    thumbnail_size = '210x150'
    medium_size = '560x390'

    def __unicode__(self):
        return self.caption

    def save(self, *args, **kwargs):
        self.date_updated = datetime.now()
        super(Photo, self).save(*args, **kwargs)
        process_images.delay(self)

    def thumbnail_image(self):
        return get_thumbnail(self.image, self.thumbnail_size)

    def medium_image(self):
        return get_thumbnail(self.image, self.medium_size)

    def processed_images(self):
        return [img() for img in (self.thumbnail_image, self.medium_image)]
