from django import forms

class FarmaceuticoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    numero=forms.IntegerField()    