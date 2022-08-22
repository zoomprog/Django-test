from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150,verbose_name='Наименование')
    content = models.TextField(blank=True,verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновленно')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Фото',blank=True)
    is_published = models.BooleanField(default=True,verbose_name='Обновленно?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,null=True,verbose_name='Категория')#models.PROTECT обеспечивает защиту от удаления

    def __str__(self):
        return self.title  # для вывода факьтческого названия объекта в консоль  вместо Object


    class Meta:
        verbose_name ='Новость'
        verbose_name_plural ='Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150,db_index=True,verbose_name='Наименование категории')

    def __str__(self):
        return self.title# дает доступ к выбору категорий


    class Meta:
        verbose_name ='Категории'
        verbose_name_plural ='Категории'
        ordering = ['title']