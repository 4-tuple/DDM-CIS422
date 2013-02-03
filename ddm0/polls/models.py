from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

class Poll(models.Model):
    question = models.CharField(max_length=200) #checking the length of the questionfield takes character
    #pub_date = models.DateTimeField('Pub Date') #renamed as Pub_date sefine as 
    fin_date = models.DateTimeField('when will this poll end?') #fin_date was defined as DateTimeField 
    pin = models.CharField(max_length=4)
    avoter = models.ForeignKey(User)
    def __unicode__(self):
        return self.question
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice

class Voter(models.Model):
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.username

#used for creating players
class VoterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100)