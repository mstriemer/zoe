from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date_created', 'date_published', 'date_updated')

admin.site.register(Post, PostAdmin)
