from django import forms
from django_clamd.validators import validate_file_infection


class UploadForm(forms.Form):
    file = forms.FileField(validators=[validate_file_infection])

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV files are allowed.")
        return file
