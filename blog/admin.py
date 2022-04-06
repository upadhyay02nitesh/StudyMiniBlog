from django.contrib import admin
from .models import Post,Study
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'title', 'desc']

@admin.register(Study)
class PostModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'title', 'desc','url1','url2',
                 'url3','url4','image']
