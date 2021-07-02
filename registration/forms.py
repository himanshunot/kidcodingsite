from django.contrib.auth import models
from registration.models import SurveyModel
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class surveyform(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(surveyform, self).__init__(*args, **kwargs)
        self.fields['srvy_rating'].widget.attrs['min'] = 1
        self.fields['srvy_rating'].widget.attrs['max'] = 10
    class Meta:
        srvy_rating = forms.IntegerField()
        srvy_desc = forms.CharField()
        
        model = SurveyModel
        fields = ('institute','srvy_rating','srvy_desc',)