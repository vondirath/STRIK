from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    description = forms.CharField(label="description", max_length=200)
    image_name = forms.CharField(label="image_name", max_length=50)
    sale = forms.BooleanField(required=False)
    featured = forms.BooleanField(required=False)
    price = forms.CharField(label="price", max_length=4)
    temporary_price = forms.CharField(label="temporary_price", max_length=4, required=False)
