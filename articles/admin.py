from django.contrib import admin

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'is_deleted', 'create_time', 'last_update_time')
    ordering = ('id',)  # 写为'-id'就会倒序排列

# admin.site.register(Article, ArticleAdmin)
