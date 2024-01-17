from django.forms import TextInput, Textarea
from django.shortcuts import get_object_or_404, render

from .models import *
from django import forms

class ticketForm(forms.ModelForm):
    model = Ticket

    place = forms.ModelChoiceField(
        queryset=Place.objects.all()
    )

    concert = forms.ModelChoiceField(
        queryset=Concert.objects.all()
    )

    class Meta:

        model = Ticket
        fields = ['first_name', 'last_name', 'concert', 'place']

        widgets = {
            "place": forms.Select(attrs={
                'class': 'input-style'
            }),
            "first_name": TextInput(attrs={
                'class': 'input-style',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'input-style',
                'placeholder': 'Фамилия'
            }),
            "concert": Textarea(attrs={
                'class': 'input-style no-visible',
                'placeholder': '',
                'value': 'ticket.concert_name',
                'readonly': 'readonly'
            })
        }

