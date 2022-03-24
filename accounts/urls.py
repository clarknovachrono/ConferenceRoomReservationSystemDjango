from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import CustomerLoginView, CustomerRegistrationView
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # built-in logout
    path('register/', CustomerRegistrationView.as_view(), name="register"),
    path('rooms/', views.room, name='rooms'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reservations/', views.reservation, name='reservation'),
    path('my_reservation/', views.my_reservation, name='my_reservation'),
    path('update_reservation/<str:pk>', views.update_reservation, name='update_reservation'),
    path('delete_reservation/<str:pk>', views.delete_reservation, name='delete_reservation'),
    path('about/', views.about_us, name='about')
]