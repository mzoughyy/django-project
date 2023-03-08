from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Resident'),
    path('contact/',views.contactus,name='contact'),


]
