from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('Resident_Dashbord/',views.home,name='Resident'),
    path('contact/',views.contactus,name='contact'),
    path('travaux/',views.travauxPage,name='travaux'),
    path('',views.send,name='homePage'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="authentication/reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="authentication/Done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="authentication/Confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="authentication/complete.html"),name="password_reset_complete"),
     path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name="authentication/ChangeDone.html"), name='password_change_done'),
    path('profile/change_password',auth_views.PasswordChangeView.as_view(template_name="Resident/profile/change_password.html"),name='change_password'),


]
