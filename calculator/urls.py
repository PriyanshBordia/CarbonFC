from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('', views.home, name='home'),
    path('member/', views.member, name='member'),
    path('find/', views.find, name='find'),
    path('search/', views.search, name='search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('calculator/', views.calculator, name='calculator'),
    path('calculator/food/', views.food, name='food'),
    path('calculator/travel/', views.travel, name='travel'),
    path('calculator/households/', views.households, name='households'),
    path('person/<int:p_id>/', views.personDetails, name='person'),
    path('person_update/', views.updatePersonDetails, name='pUpdate'),
    path('persons/', views.allPersons, name='persons'),
    path('user/<int:user_id>/', views.userDetails, name='user'),
    path('user_update/', views.updateUserDetails, name='uUpdate'),
    path('users/', views.allUsers, name='users'),
    # path('login', views.login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
