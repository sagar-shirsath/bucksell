from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
GENDER_SELECT = ((1,'Male'),(2,'Female'),(3,'Other'))
DEGREE_CHOICES = (("",'---'),('MSC','Msc'),('BSC','Bsc'),('12th','12th'),('10th','10th'))
YEAR_CHOICES  = ((0,"---"),(1987,1987),(1988,1989),(2000,2000),(2001,2001))
VISIBILITY_CHOICES = ((1,'Every One'),(2,'Same City'),(3,'People Made deal with me'),(4,'nobody'))
UNIVERSITY_CHOICES = ('','---',('pune','PUNE'),('mumbai','MUMBAI'))
class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length=30,required=False)
    about_me = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':20}),required=False)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_SELECT,required=False)
    degree_pursuing = forms.CharField(max_length=5,widget=forms.Select(choices=DEGREE_CHOICES),required=False)
    year_of_class = forms.IntegerField(widget=forms.Select(choices=YEAR_CHOICES),required=False)
    current_password = forms.CharField(widget=forms.PasswordInput,required=False)
    new_password = forms.CharField(widget=forms.PasswordInput,required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput,required=False)
    phone_number = forms.CharField(required=False)
    address = forms.CharField(required=False)
    university = forms.CharField(required=False,widget=forms.Select(choices=UNIVERSITY_CHOICES))
    paypal_url = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    visibility = forms.ChoiceField(widget=forms.RadioSelect, choices=VISIBILITY_CHOICES,required=False)


class ImageUploadForm(forms.Form):
    """Image upload form."""
    photo = forms.ImageField()