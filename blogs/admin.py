from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'last_updated')

    search_fields = ('title', 'author__username', 'hashtags__tag')
    readonly_fields = ('published_date', 'last_updated', 'hashtags')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = ()


admin.site.register(Blog, BlogAdmin)
