from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.views import (PasswordChangeView,LoginView,PasswordResetView,
                                       PasswordResetDoneView,PasswordResetConfirmView)
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth import logout

from .forms import ResgisterForm,ChangePasswordForm
from .models import User

# Create your views here.
def home(request):
    return render(request,'index.html')


class RegisterUser(CreateView):
    model = User
    form_class = ResgisterForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')


class LoginView_(LoginView):
    # form_class = LoginForm
    template_name = 'login.html'
    success_url =reverse_lazy('home')
    # redirect_authenticated_user = True
    authentication_form = AuthenticationForm


class LogoutView_(View):
    
    def get(self,request):
        logout(request)
        return redirect('home')
    

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'restaurant-change-password.html'
    success_url = reverse_lazy('home')


class ResetPasswordView(PasswordResetView):
    template_name = 'reset_password.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    from_email = 'pakwanonline@gamil.com'


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'resset_password_done.html'


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password_comfirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('login')


# def register(request):
#     form = ResgisterForm()
#     if request.method == 'POST':
#         form = ResgisterForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             return render(request,'index.html',{'form':form,'message':'success'})
#         else:
#             return render(request,'registration.html',{'form':form})
    
#     return render(request,'registration.html',{'form':form})
