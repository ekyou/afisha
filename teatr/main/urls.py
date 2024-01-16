from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainSite, name='home'),
    path('afisha/', views.afishaSite, name='afisha'),
    path('tickets/<int:concert_id>', views.ticketsSite, name='tickets'),
    path('contacts/', views.contactsSite, name='contacts'),
    path('afisha/<int:concert_id>/', views.showAfisha, name='more_info'),
]