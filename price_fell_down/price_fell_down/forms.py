from django import forms

class MyForm(forms.Form):
    product_link = forms.CharField()
    price = forms.CharField()
    email = forms.EmailField(label='E-Mail')

