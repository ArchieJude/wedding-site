from django import forms
from .models import RSVP


class RSVPForm(forms.ModelForm):
    attendance = forms.ChoiceField(choices=RSVP.ATTENDANCE_CHOICES, required=True)

    class Meta:
        model = RSVP
        fields = [
            'name', 'email', 'attendance',
            'number_in_party', 'dietary_notes', 'song_request', 'message',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'number_in_party': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'dietary_notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Allergies or dietary restrictions'}),
            'song_request': forms.TextInput(attrs={'placeholder': 'Artist — Song title (optional)'}),
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Leave a note for us (optional)'}),
        }
