from numpy.f2py.crackfortran import requiredpattern
from items.models import Item
from django import forms

CATEGORY_SELECT = ((1,'Books'),(2,'Music'),(3,'Service'))
CONDITION_CHOICES = ((1,'Mint'),(2,'Like New'),(3,'Fair'))
class ItemForm(forms.Form):
	item_name = forms.CharField(max_length=30,required=True)
	price = forms.CharField(max_length=30,required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':20}),required=True)
	condition = forms.ChoiceField(widget=forms.RadioSelect, choices=CONDITION_CHOICES,required=True)
	category = forms.IntegerField(widget=forms.Select(choices=CATEGORY_SELECT),required=True)
	longitude = forms.HiddenInput()
	latitude = forms.HiddenInput()

class ImageUploadForm(forms.Form):
	"""Image upload form."""
	photo = forms.ImageField()