from django import forms
from django.core import validators
class Job_Application_form(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    email = forms.EmailField( validators=[validators.MinLengthValidator(3)] )
    contact_number = forms.IntegerField()
    linkedIn_Url = forms.CharField(validators=[validators.MinLengthValidator(5)])
    github = forms.CharField(validators=[validators.MinLengthValidator(5)])
    more_info = forms.CharField(widget= forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        contact_number_input = cleaned_data['contact_number']
        
        
        more_info_input = cleaned_data['more_info']
        if len(more_info_input)< 5:
            raise forms.ValidationError("Enter minimum 1 information")
        






