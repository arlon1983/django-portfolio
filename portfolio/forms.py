from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'project_type', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@company.com',
                'class': 'form-input',
            }),
            'project_type': forms.TextInput(attrs={
                'placeholder': 'CRM, inventory, booking, insurance...',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me about your project',
                'class': 'form-input',
                'rows': 5,
            }),
        }
