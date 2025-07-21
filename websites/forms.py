from django import forms

class WebsiteForm(forms.Form):
    name = forms.CharField(label='Enter Text or URL', max_length=350)