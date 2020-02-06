from django import forms
from .models import good, interface, kit_interface, cables

class GoodForm(forms.ModelForm):

    class Meta:
        model = good
        fields = '__all__'  