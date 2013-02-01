from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=200) #checking the length of the questionfield takes character
    #pub_date = models.DateTimeField('Pub Date') #renamed as Pub_date sefine as 
    fin_date = models.DateTimeField('when will this poll end?') #fin_date was defined as DateTimeField 
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.fin_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'fin_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice