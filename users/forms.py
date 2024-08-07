from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from shop.bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    first_name = forms.CharField(label="Write your firs name")
    last_name = forms.CharField(label="Write your last name")
    username = forms.CharField(label='Write your username')
    email = forms.EmailField(label='Write your email')
    password1 = forms.CharField(label='Create a password')
    password2 = forms.CharField(label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(BulmaMixin, forms.ModelForm):
    email = forms.EmailField(label='Write your Email')
    first_name = forms.CharField(label='Write your First name')
    last_name = forms.CharField(label='Write your Last name')
    username = forms.CharField(label='Write your Username')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']


class ChangePasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']










