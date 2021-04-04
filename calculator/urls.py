from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('calculator', views.calculator, name='calculator'),
    path('calculator/food', views.food, name='food'),
    path('calculator/travel', views.travel, name='travel'),
    path('calculator/households', views.households, name='households'),
    path('user', views.user, name='user'),
    path('users', views.users, name='users'),
    # path('login', views.login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
