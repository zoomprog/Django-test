from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at','is_published')
    list_display_links = ('id','title')#указывает какие модели будут являтся ссылками
    search_fields = ('title','content')#добовляет поиск в админке


admin.site.register(News,NewsAdmin)