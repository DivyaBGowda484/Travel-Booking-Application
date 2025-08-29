from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('', views.booking_list, name='booking_list'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]