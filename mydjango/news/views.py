from django.shortcuts import render
from django.http import HttpResponse

from .models import News,Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,

    }
    return render(request,template_name='news/index.html', context=context)

def get_categoty(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    return render(request,'news/category.html', {'news': news,'categories':categories,'category':category })
