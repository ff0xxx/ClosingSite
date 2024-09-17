from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from closingsite import settings
from clothing import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clothing.urls', namespace='clothing')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),

    path('add/', views.ClothingCreateView.as_view(), name='add'),
    path('cart/', include('carts.urls', namespace='cart'))
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

