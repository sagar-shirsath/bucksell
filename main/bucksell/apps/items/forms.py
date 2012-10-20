from items.models import Item
from django import forms
from categories.models import Category

CONDITION_CHOICES = ((1, 'Mint'), (2, 'Like New'), (3, 'Fair'))

class ItemForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}))
    condition = forms.ChoiceField(widget=forms.RadioSelect, choices=CONDITION_CHOICES)
    price = forms.CharField(max_length=30)
    longitude = forms.CharField(widget=forms.HiddenInput,required=False)
    latitude = forms.CharField(widget=forms.HiddenInput,required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.filter())
    image1 = forms.ImageField()
    image2 = forms.ImageField()
    image3 = forms.ImageField()


class ImageUploadForm(forms.Form):
    """Image upload form."""
    photo = forms.ImageField()