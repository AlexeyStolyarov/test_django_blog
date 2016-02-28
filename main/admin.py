from django.contrib import admin

from main.models import BlogItem
from main.models import BlogItemComment

class BlogItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    
admin.site.register(BlogItem, BlogItemAdmin)
admin.site.register(BlogItemComment)

