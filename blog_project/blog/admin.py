from django.contrib import admin
from blog.models import Post,Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('title','author','created','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','body','created','post','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')


admin.site.register(Comments,CommentAdmin)
admin.site.register(Post,PostAdmin)
