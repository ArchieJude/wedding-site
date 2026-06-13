from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('rsvp/thanks/', views.rsvp_confirm, name='rsvp_confirm'),
    path('gallery/', views.gallery, name='gallery'),
    path('schedule/', views.schedule, name='schedule'),
    path('travel/', views.travel, name='travel'),
    path('faq/', views.faq, name='faq'),
]
