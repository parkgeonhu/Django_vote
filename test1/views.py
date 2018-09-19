# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from models import RestDayParty

# Create your views here.




def post_publish(request, pk):
    rest_day_party = get_object_or_404(RestDayParty, pk=pk)
    rest_day_party.publish()
    return redirect('rest_day_party_detail', pk=pk)
