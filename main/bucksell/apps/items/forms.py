from items.models import Item
from django import forms
from categories.models import Category

CONDITION_CHOICES = ((1, 'New'), (2, 'Pretty Good'), (3, 'Gets the Job Done'),(4,'Looks that only a Mother could Love'))
IS_SERVICE_CHOICES = ((0, 'Item'), (1, 'Service'))

class ItemForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}))
    condition = forms.ChoiceField(widget=forms.RadioSelect, choices=CONDITION_CHOICES,required=False)
    is_service = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'is_service'}), choices=IS_SERVICE_CHOICES,required=False)
    price = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'In $'}))
    longitude = forms.CharField(widget=forms.HiddenInput,required=False)
    latitude = forms.CharField(widget=forms.HiddenInput,required=False)
    location = forms.CharField(widget=forms.HiddenInput,required=False)
    pincode = forms.CharField(widget=forms.HiddenInput,required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.filter().order_by('id'))
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)


class ImageUploadForm(forms.Form):
    """Image upload form."""
    photo = forms.ImageField()