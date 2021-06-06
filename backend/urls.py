from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('backend.api.urls')),
    # Эндпоинт для SPA
    re_path(r'^(?!api|static|admin|media).*$', TemplateView.as_view(template_name="index.html")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


