from authentication.views import logout
from django.urls import path
from .views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register',views.register,name="register"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('profile',views.profile_page,name='profile'),
    path('profile/edit',views.edit_profile,name='edit_profile'),
    path('send_sms/', views.send_sms_view, name='send_sms'),
    


]+static(settings.STATIC_ROOT,document_root=settings.STATIC_ROOT)
