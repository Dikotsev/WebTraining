from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)





class SignInForm(forms.Form):
     username = forms.CharField(
         max_length=10,
     )
     password= forms.CharField(
         max_length=10,
         widget= forms.PasswordInput(),
     )

     def CleanedPassword(self):
        self.user = authenticate(
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password'],

        )

        if not self.user:
            raise  ValidationError('email / password is incorrect ')


     def save(self):
         return self.user