from .models import Event
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        

class ParticipantListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username
    
    def to_internal_value(self, data):
        try:
            try:
                return User.objects.get(username=data)
            except KeyError:
                raise serializers.ValidationError(
                    'id is a required field.'
                )
            except ValueError:
                raise serializers.ValidationError(
                    'id must be an integer.'
                )
        except User.DoesNotExist:
            raise serializers.ValidationError(
            'Obj does not exist.'
            )    

class EventSerializer(serializers.HyperlinkedModelSerializer):
    participants = ParticipantListingField(queryset=User.objects.all(), many=True)
    
    class Meta:
        model = Event
        fields = '__all__' 
    # class Meta:
    #     model = Event
    
    
    #     fields = ('first_name', 'last_name')
    
    #https://www.reddit.com/r/django/comments/6yrh9k/drf_serialization_not_working_on_many_to_many/

        
    
    