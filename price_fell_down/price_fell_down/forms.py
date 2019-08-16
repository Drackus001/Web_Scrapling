from django import forms

class MyForm(forms.Form):
    url = forms.CharField()
    price = forms.CharField()
    email = forms.EmailField(label='E-Mail')

