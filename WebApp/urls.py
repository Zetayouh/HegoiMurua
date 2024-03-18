from django.urls import path

from . import views
from proyectos.views import selecciona_proyecto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('proyectos/<int:proyecto_id>/', selecciona_proyecto, name="selecciona_proyecto")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)