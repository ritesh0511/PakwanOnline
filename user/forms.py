from typing import Any
from django import forms
from django.core.validators import RegexValidator

from .models import User,UserProfile,Address 


class ResgisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),validators=[RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$&*?])[a-zA-Z\d!@#$&*?]{6,}',message="Please enter validator valid password.")])
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField(validators=[RegexValidator(regex=r'^([789])?\d{10}$',message='Please enter validator valid phone number')])
    # mobil = models.IntegerField(validators=[RegexValidator(regex=r'^([789])?\d{10}$',message='Enter a valid mobile number')],unique=True)
    

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','phone','role']


    def clean(self) -> dict[str, Any]:
        cleaned_data = super(ResgisterForm,self).clean()
        if self.is_valid() and cleaned_data['password'] != cleaned_data['confirm_password'] :
            raise forms.ValidationError('Password did not matched')
        return cleaned_data

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        # user.full_clean()
        if commit:
            user.save()
        return user
    
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        if self.is_valid() and cleaned_data['new_password'] == cleaned_data['confirm_passwoed']:
            raise forms.ValidationError('Confirm Password did not matched.')
        return cleaned_data
    

# class LoginForm(forms.Form):
#     email = forms.CharField(max_length=20)
#     password = forms.CharField(widget=forms.PasswordInput())
    
        
        