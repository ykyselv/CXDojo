from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class DataCollectorForm(forms.Form):
    csv_file_path = forms.CharField(label='path_to_csv_file', max_length=100)
    xml_file_path = forms.CharField(label='path_to_xml_file', max_length=100)
