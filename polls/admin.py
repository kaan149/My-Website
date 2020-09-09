from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('article_title',)

admin.site.register(Article, ArticleAdmin)
# Register your models here.
