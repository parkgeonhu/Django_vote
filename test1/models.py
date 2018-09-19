# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from vote.models import VoteModel
from django.utils import timezone

class RestDayParty(VoteModel, models.Model):
    MEETING_LOCATIONS = (
        ('원통', '원통'),
        ('서화', '서화'),
    )
    meeting_location = models.CharField(
        max_length=2,
        choices=MEETING_LOCATIONS,
        default='원통',
    )
    startDay = models.DateField(u'Day of the event', help_text=u'Day of the event')
    content = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    def publish(self):
        self.pub_date = timezone.now()
        self.save()
        

class Parcipate_list(models.Model):
    participant = models.ForeignKey(User, verbose_name = u'account', on_delete = models.PROTECT)
    party = models.ForeignKey(RestDayParty,  verbose_name = u'pk', on_delete = models.PROTECT)






