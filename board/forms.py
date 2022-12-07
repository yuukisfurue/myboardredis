from django import forms

class BoardForm(forms.Form):
    name = forms.CharField(label='name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='address', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))