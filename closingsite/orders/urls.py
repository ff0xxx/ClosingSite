from django.urls import path
from orders import views


app_name = 'orders'

urlpatterns = [
    # кнопка мелкой корзины не работает!!
    # а без нее перед адресом прописывается еще чето (user~)
    # РАЗБЕРИСЬ НАКОНЕЦ ПОЧЕМУ ОНА НЕ РАБОТАЕТ!!!!
    path('create-order/', views.create_order, name='create_order')
]
