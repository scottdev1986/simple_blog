from django.contrib import admin

from . models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'is_published', 'published_date')
    list_display_links =('id', 'author')
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(Article, ArticleAdmin)


