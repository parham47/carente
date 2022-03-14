import datetime

from django import forms
from django.core.exceptions import ValidationError
from .models import cars

class SendcarsForm(forms.ModelForm):
    class Meta:
        model = cars
        exclude = ['available']
       

    ##def clean_published_at(self:
        #date = self.cleaned_data['published_at']

      #  if date <= datetime.datetime.today() :
       #     raise ValidationError('تاریخ وارد شده نباید کوچکتر از زمان امروز باشد'

        #return date