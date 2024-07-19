from django.contrib import admin
from .models import NewsArticle

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author', 'content')
    list_filter = ('published_date', 'tags')

admin.site.register(NewsArticle, NewsArticleAdmin)