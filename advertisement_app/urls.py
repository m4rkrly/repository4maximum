
from django.urls import path
from .views import index, home, top_sellers, advertisement_post, register, login, profile

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', index, name = 'index'),
    path('', home, name = 'home'),
    path('top_sellers/', top_sellers, name = "top_sellers"),
    path('advertisement_post/', advertisement_post, name = 'advertisement_post'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('profile/', profile, name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)