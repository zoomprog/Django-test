from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')  # указывает какие модели будут являтся ссылками
    search_fields = ('title', 'content')  # добовляет поиск в админке
    list_editable = ('is_published',)# добавляет чекбоксы
    list_filter = ('is_published','category')#добавляет фильтр в админку


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  # указывает какие модели будут являтся ссылками
    search_fields = ('title',)  # добовляет поиск в админке


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
