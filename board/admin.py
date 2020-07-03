from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','OS','title','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text','created','os']
    ordering = ['updated','created']

admin.site.register(Post,PostAdmin )