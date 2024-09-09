from django.contrib import admin
from django.urls import path, include

from closingsite.settings import DEBUG
from clothing import views

# root - bob@mail.ru - 1234

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clothing.urls', namespace='clothing')),
    path('catalog/', include('goods.urls', namespace='catalog')),

    path('add/', views.ClothingCreateView.as_view(), name='add')
]

if DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]
