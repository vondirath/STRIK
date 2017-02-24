from django import forms


class ContactForm(forms.Form):
    """
        Returns the content to be rendered for the form page.
    """
    subject = forms.CharField(label="Your name", max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    Email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
