from .models import Note
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Not more than 50 charcters',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Not more than 500 characters',
            }),
        }
        labels = {
            'name': 'Title',
        }
