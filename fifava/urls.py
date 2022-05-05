
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
]


handler404 = "base.views.Bulunamadi"
handler500 = "base.views.Hata"