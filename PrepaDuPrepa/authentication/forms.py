from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    role = forms.ChoiceField(choices=(
        ('ROLE_STUDENT', 'Student'),
        ('ROLE_TEACHER', 'Teacher')
    ), widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            })
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        custom_user = CustomUser(user=user)
        custom_user.email = self.cleaned_data['email']
        custom_user.roles = self.cleaned_data['role']
        if commit:
            custom_user.save()
        return user
