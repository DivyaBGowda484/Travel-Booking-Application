from django import forms
from .models import TravelOption

class TravelOptionForm(forms.ModelForm):
    class Meta:
        model = TravelOption
        fields = ['type', 'source', 'destination', 'date_time', 'price', 'available_seats']
