from django import forms
from . models import Contact
from django.forms import TextInput ,  EmailInput , Textarea 

class ContactForm(forms.ModelForm):
 class Meta:
        model = Contact
        fields = ['name' , 'email' , 'phone' , 'subject' , 'message' ]
        widgets = {
            'name' : TextInput(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Your Name'}),       
            'email' : EmailInput(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Your E-mail'}),
            'phone' : TextInput(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Enter Your Subject'}),
            'subject' : TextInput(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Enter Your Subject'}),
            'message' : Textarea(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Please explain Your Problem'}), 
            }
    
