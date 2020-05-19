from django import forms
class UserForm(forms.Form):
    poolin = forms.CharField(max_length=100)
