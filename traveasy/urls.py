from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('home.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('cars/', include('cars.urls')),
    path('', include ('contact.urls')),
    path('', include ('registration.urls')),
    path('cart/', include('cart.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('adminpanel/', include('adminpanel.urls')),
    path('',include('user.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)