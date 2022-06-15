from .views import RegistrationView, UsernameValidationView, EmailValidationView, LoginView, LogoutView, AboutView, ProfileView
from . import views
from django.urls import path

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('profile', ProfileView.as_view(), name="profile"),
    path('about', AboutView.as_view(), name='about'),

    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate_email'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html')
         ,name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
        (template_name='authentication/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),

    ]