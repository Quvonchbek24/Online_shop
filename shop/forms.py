from django import forms
from .models import Order, Review, RATE_CHOICES
from .bulma_mixin import BulmaMixin


class OrderForm(BulmaMixin, forms.Form):
    address = forms.CharField(label='Write your address')
    phone = forms.CharField(label='Write your phone number')

    class Meta:
        model = Order
        fields = ['phone', 'address']


class RateForm(BulmaMixin, forms.ModelForm):
    text = forms.CharField(label='Write your text')
    rate = forms.ChoiceField(choices=RATE_CHOICES, required=True, label='Rate product from 1 to 5')

    class Meta:
        model = Review
        fields = ('text', 'rate')



