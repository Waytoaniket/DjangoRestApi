from rest_framework import serializers 
from API.models import Advisor, Users, CallBooked
 
 
class AdvisorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Advisor
        fields = ('Id',
                  'Name',
                  'Photourl')

class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Users
        fields = ('Id',
                  'Name',
                  'Email',
                  'Password')

class UserLoginSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Users
        fields = ('Id',
                  'Email',
                  'Password')

class CallBookedSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CallBooked
        fields = ('Id',
                  'Advisor',
                  'User',
                  'Time')