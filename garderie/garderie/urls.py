from accueil.views import index, detail_views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from contact import views as contact_views
from garderie import settings

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('detail/', detail_views, name="detail"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


