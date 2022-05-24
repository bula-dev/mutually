from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from api import views

urlpatterns = [
    path('user', views.UserView.as_view()),
    path('like', views.LikeView.as_view()),
    path('profile', views.ProfileView().as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# images are saved found at urls according to ...localhost:8000/profiles/media/images/...
