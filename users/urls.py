from django.urls import path
from .views import sign_up, sign_in, sign_out, edit_profile, reset_password

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('sign-in/', sign_in, name='sign_in'),
    path('sign-out/', sign_out, name='sign_out'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('reset-password/', reset_password, name='reset_password'),
]
