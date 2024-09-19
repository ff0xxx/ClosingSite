from django import template
from carts.utils import get_user_carts

register = template.Library()


# возвращает все таблицы-заказы юзера
@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)
