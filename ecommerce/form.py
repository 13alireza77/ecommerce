from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class contactForm(forms.Form):
    fullName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    contact = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Youre Message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class registerForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='confirm password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists:
            raise forms.ValidationError("username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists:
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError("passwords must match.")
        return data
