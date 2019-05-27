from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls


urlpatterns = [

    # Core
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Django REST')),

    # API 
    url(r'^', include('messenger.urls' , namespace="messenger")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
