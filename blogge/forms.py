from django import forms
from .models import Contact

#1-usul
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__" #('name','email','message')
        
# #2-usul
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField(max_length=255)
#     message = forms.Textarea()