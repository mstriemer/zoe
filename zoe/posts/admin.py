from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from posts.models import Post, Photo

class InlinePhotoAdmin(AdminImageMixin, admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date_created', 'date_published', 'date_updated')
    inlines = (InlinePhotoAdmin,)

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)
