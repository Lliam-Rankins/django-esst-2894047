from django.core.exceptions import ValidationError

from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'rounded border px-3 my-5 text-2xl'}),
            'text': forms.Textarea(attrs={'class': 'rounded border px-3 my-5 text-2xl'})
        }
        labels = {
            'text': 'Write your thoughts here'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        # if "Django" not in title:
        #     raise ValidationError("We only accept notes about Django")
        return title