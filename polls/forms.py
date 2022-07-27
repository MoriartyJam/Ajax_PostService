from django import forms
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name',)

    def clean_name(self):
        name = self.cleaned_data['name'].capitalize()

        if Pet.objects.filter(name=name).exists():
            raise forms.ValidationError('')

        return name
