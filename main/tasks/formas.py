from django import forms


class SendAsyncEmailForm(forms.Form):
    send_to = forms.EmailField(label="Recipient Email", max_length=254)
    subject = forms.CharField(label="Subject", max_length=255)
    body = forms.CharField(label="Body", widget=forms.Textarea)
