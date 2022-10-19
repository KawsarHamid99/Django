from django import forms


class studentClass(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
