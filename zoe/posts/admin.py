from django.contrib import admin

from posts.models import Post, Photo


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date_created', 'date_published', 'date_updated')


class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)
