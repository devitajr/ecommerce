from django import forms

class PayForm(forms.Form):
    name = forms.CharField()
    password = forms.IntegerField()
    adress = forms.CharField()
    cep = forms.CharField()
    city = forms.CharField()
    card = forms.CharField()
    date = forms.DateField()
    cvv = forms.CharField()