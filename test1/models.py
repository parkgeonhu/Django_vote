# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from vote.models import VoteModel

class ArticleReview(VoteModel, models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')




