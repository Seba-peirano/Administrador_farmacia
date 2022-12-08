from django import forms

class FarmaceuticoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    num_vendidos=forms.IntegerField()

class FabricanteForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    email=forms.EmailField()
    
class RemedioForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    droga=forms.CharField(max_length=50)
    vencimiento=forms.DateField()
 