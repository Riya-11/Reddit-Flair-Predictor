from django import forms


class urlForm(forms.Form):
    post_url = forms.CharField(label='Enter the url', max_length=10000)
