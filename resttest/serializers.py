from .models import Event
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        

class EventSerializer(serializers.HyperlinkedModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Event
        fields = '__all__' 
    # class Meta:
    #     model = Event
    #     fields = ('first_name', 'last_name')
    
    #https://www.reddit.com/r/django/comments/6yrh9k/drf_serialization_not_working_on_many_to_many/

        
    
    