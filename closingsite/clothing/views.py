from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView

from goods.models import Categories
from django.shortcuts import render
from django.views.generic.edit import CreateView


def index(request):
    # categories = Categories.objects.all()

    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
        # 'categories': categories,
    }
    return render(request, 'clothing/index.html', context)


# class ClothingList(ListView):
#     template_name = 'clothing/index.html'
#     context_object_name = 'clth'
#
#     def get_queryset(self):
#         return ClothingModel.objects.all()


def about(request):
    context = {
        'title': 'О сайте',
        'content': 'Это сайт магазин-мебели',
        'text_on_page': 'Смотрите, заказывайте. Поддерживайте экономику.'
    }
    return render(request, 'clothing/about.html', context)


