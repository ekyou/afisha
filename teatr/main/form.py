from django.forms import TextInput, DateInput, DateTimeInput, SelectDateWidget
from django.shortcuts import get_object_or_404, render

from .models import *
from django import forms

class ticketForm(forms.ModelForm):
    model = Ticket
    date_format = forms.DateField(
        widget=forms.DateInput(format='%d%m%Y'),
        input_formats=['%d%m%Y'],
    )

    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'concert', 'price', 'place']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'input-style',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'input-style',
                'placeholder': 'Фамилия'
            }),
            "concert": TextInput(attrs={
                'class': 'input-style',
                'placeholder': '',
                'value': 'ticket.concert_name',
                'readonly': 'readonly'
            }),
            "price": TextInput(attrs={
                'class': 'input-style',
                'placeholder': '',
                'value': 'ticket.price',
                'readonly': 'readonly'
            }),
            "place": TextInput(attrs={
                'class': 'input-style',
                'placeholder': '',
                'value': '',
                'readonly': 'readonly'
            }),
            "date_time": TextInput(attrs={
                'class': 'input-style',
                'placeholder': '',
                'value': 'time.date_time',
                'readonly': 'readonly'
            }),
        }