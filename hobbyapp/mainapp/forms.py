from django import forms
from mainapp.models import Users
class UpdateForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = [
            'name',
        ]