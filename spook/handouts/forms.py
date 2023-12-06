from django import forms

class HandoutForm(forms.Form):
    full_name = forms.CharField(max_length = 200)
    contents_text = forms.CharField(label="Handout text", max_length=700, widget=forms.Textarea)
