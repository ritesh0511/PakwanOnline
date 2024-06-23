from django.urls import path
from .views import (RegisterUser,home,ChangePasswordView,LoginView_,LogoutView_,ResetPasswordView,
                    ResetPasswordDoneView,ResetPasswordConfirmView)

urlpatterns = [
    path('',home,name='home'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('login/',LoginView_.as_view(),name='login'),
    path('logout/',LogoutView_.as_view(),name='logout'),
    path('change_password/',ChangePasswordView.as_view(),name='change_password'),
    path('reset_password/',ResetPasswordView.as_view(),name='reset_password'),
    path('password_reset_done/',ResetPasswordDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',ResetPasswordConfirmView.as_view(),name='password_reset_confirm'),



]