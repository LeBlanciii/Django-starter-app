from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='landing.html'), name='landing'),
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
