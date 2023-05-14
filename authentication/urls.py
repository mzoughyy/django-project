from authentication.views import logout
from django.urls import path
from .views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import view_payments

urlpatterns = [
 path('admin/send-email/', views.send_email_admin, name='send_email_admin'),
    path('register',views.register,name="register"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('profile',views.profile_page,name='profile'),
    path('profile/edit',views.edit_profile,name='edit_profile'),

    path('send_sms/', views.send_sms_view, name='send_sms'),
    path('sent_msg/<int:pk>/', views.sentMessages, name='sent_msg'),
    path('chat/', views.index, name= "index"),
    path('friend/<str:pk>', views.detail, name="detail"),
    path('sent_msg/<int:pk>/', views.sentMessages, name='sent_msg'),
    path('rec_msg/<str:pk>', views.receivedMessages, name = "rec_msg"),
    path('notification', views.chatNotification, name = "notification"),
    path('payments/', view_payments, name='view_payments'),


]+static(settings.STATIC_ROOT,document_root=settings.STATIC_ROOT)
