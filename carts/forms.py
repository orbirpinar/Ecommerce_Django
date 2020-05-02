from django import forms

from django_countries.widgets import CountrySelectWidget

from .models import Adress

class AdressForm(forms.ModelForm):

    class Meta:
        model = Adress
        fields = "__all__"
        widgets = {'country': CountrySelectWidget(),
                    'street_adress':forms.TextInput(attrs = {'class':'form-control'}),
                    'apartment_adress':forms.TextInput(attrs = {'class':'form-control'}),
                    'zip_code':forms.TextInput(attrs = {'class':'form-control'})
        
        }


    