# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.

class Event(models.Model):
    LOCATIONS = (
        ('원통', '원통'),
        ('서화', '서화'),
    )
    WAYS = (
        ('taxi', 'taxi'),
        ('carpool', 'carpool'),
    )
    meeting_location = models.CharField(
        max_length=2,
        choices=LOCATIONS,
        default='서화',
    )
    arrival_location = models.CharField(
        max_length=2,
        choices=LOCATIONS,
        default='원통',
    )
    way = models.CharField(
        max_length=4,
        choices=WAYS,
        default='taxi',
    )
    
    departure_date = models.DateField(u'출발날짜', help_text=u'출발날짜', null=True)
    content = models.TextField(u'게시물 내용', help_text=u'게시물 내용', blank=True, null=True)
    
    participants = models.ManyToManyField(User)
    
    published_date = models.DateTimeField('date published', null=True)
    
    def __str__(self):
        return str(self.pk)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        
class Comment(models.Model):
    post = models.ForeignKey(Event, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
        

