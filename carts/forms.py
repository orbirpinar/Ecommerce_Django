from django import forms

from django_countries.widgets import CountrySelectWidget

from .models import Adress,Customer

ADRESS_FIELDS = (
    ('B','Billing'),
    ('S', 'Shipping')
)




class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['street_adress','apartment_adress','country','city','zip_code','adress_type']
        widgets = {'country': CountrySelectWidget(),
                    'street_adress':forms.TextInput(attrs = {'class':'form-control'}),
                    'apartment_adress':forms.TextInput(attrs = {'class':'form-control'}),
                    'zip_code':forms.TextInput(attrs = {'class':'form-control'}),
                    'name':forms.TextInput(attrs = {'class':'form-control'}),
                    'email':forms.TextInput(attrs = {'class':'form-control','id':'email'}),
                    
        
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','email')
    