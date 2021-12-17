from django import forms
from .models import Laptop
class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        widgets={
            'company':forms.TextInput(
                attrs={
                    'placeholder':'Enter Company Name'
                }
            ),
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Model Name'
                }
            ),
            'ram': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Ram of Laptop'
                }
            ),
            'rom': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Rom of Laptop'
                }
            ),
            'processor': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Processor'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Price Of Laptop'
                }
            ),
            'weight': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Weight of Laptop'
                }
            )
        }

    def clean_ram(self):
        m=self.cleaned_data['ram']
        if m % 2 ==1:
            raise forms.ValidationError('RAM must be in Even Digits')
        elif m < 1 :
            raise forms.ValidationError('RAM must be greater than one')
        else:
            return m

    def clean_company(self):
        company = self.cleaned_data['company']
        if company.istitle():
            return company
        else:
            raise forms.ValidationError('First letter should be capital')
    def clean_model_name(self):
        model_name = self.cleaned_data['model_name']
        if model_name.istitle():
            return model_name
        else:
            raise forms.ValidationError('First letter should be capital')

    def clean_rom(self):
        m=self.cleaned_data['rom']
        if m < 100:
            raise forms.ValidationError('ROM must be in Greater than 100 GB')
        else:
            return m
    def clean_price(self):
        m=self.cleaned_data['price']
        if m < 20000 :
            raise forms.ValidationError('Price should be greater than 20000')
        elif m > 150000 :
            raise forms.ValidationError('Price should be less than 150000')
        else:
            return m
