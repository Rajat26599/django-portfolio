from django import forms

class ContactForm(forms.Form):
        name = forms.CharField(label='Your name')
        email = forms.EmailField(label='Your Email')
        text = forms.CharField(widget=forms.Textarea)
