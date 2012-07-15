from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','enable_comments', 'status')
    search_fields = ['title', 'body']
    list_filter = ('pub_date', 'enable_comments', 'status')
    prepopulated_fields = {"slug" : ('title',)}
    fieldsets = (
		(None, {'fields': (('title', 'status'), 'body', ('pub_date', 'enable_comments'), 'tags', 'slug')}),
    )


admin.site.register(Post, PostAdmin)
