from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import api.views

urlpatterns = [
    path("users/", api.views.UserView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# images are saved found at urls according to ...localhost:8000/profiles/media/images/...
