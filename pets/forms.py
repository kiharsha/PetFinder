from django import forms
from .models import Pet

class LostPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'pet_type', 'description', 'image']


class ImageSearchForm(forms.Form):
    image = forms.ImageField()
