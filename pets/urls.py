from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('test/', lambda request: HttpResponse("Pets app works")),
    path('add-lost-pet/', views.add_lost_pet, name='add_lost_pet'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('search/', views.search_pet, name='search_pet'),
]
