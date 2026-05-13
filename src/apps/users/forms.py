from django import forms
from django.contrib.auth import authenticate
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'w-full pl-11 pr-4 py-3.5 bg-white rounded-xl text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 font-medium border border-slate-200',
        'placeholder': 'Enter your email'
    }))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={
        'class': 'w-full pl-11 pr-12 py-3.5 bg-white rounded-xl text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 font-medium border border-slate-200',
        'placeholder': 'Enter your password'
    }))

    def save(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(username=email, password=password)
        return user


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={
        'class': 'w-full pl-11 pr-12 py-3.5 bg-white rounded-xl text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 font-medium border border-slate-200',
        'placeholder': 'Create a password'
    }))

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full pl-11 pr-4 py-3.5 bg-white rounded-xl text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 font-medium border border-slate-200',
                'placeholder': 'Enter your phone number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full pl-11 pr-4 py-3.5 bg-white rounded-xl text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 font-medium border border-slate-200',
                'placeholder': 'Enter your email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full pl-11 pr-4 py-3.5 bg-white rounded-xl text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 font-medium border border-slate-200',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full pl-11 pr-4 py-3.5 bg-white rounded-xl text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 font-medium border border-slate-200',
                'placeholder': 'Last name'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

