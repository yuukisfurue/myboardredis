from django import forms
from.models import Friend

class BoardForm(forms.Form):
    name = forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Address', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.CharField(label='Gender', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='Age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    jyob = forms.DateField(label='Jyob', \
        widget=forms.DateInput(attrs={'class':'form-control'}))

class FindForm(forms.Form):
        find = forms.CharField(label='Find', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','address','gender','age','jyob']
        