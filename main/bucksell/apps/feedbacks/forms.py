from django import forms

class FeedbckForm(forms.Form):
    subject = forms.CharField(  required = False)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':20}) , required=False)


