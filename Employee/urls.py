from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect


urlpatterns = [
      path('', lambda request: redirect('/home/')),
    path('admin/', admin.site.urls),
    path('home/', include('emp.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)