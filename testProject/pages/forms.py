from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(UserCreationForm):
    username = forms.CharField()
    image = forms.ImageField(required=False)
    bio = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'image', 'bio', )

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.bio = self.cleaned_data["bio"]
        if commit:
            user.save()
        return user
