from django.db import models
from django.forms import forms

from WebTraining.customer_profile.models import Profile



class ProfileForm(forms.ModelForms):
    class Meta:
        model = Profile
        exclude = ('user',)
