from rest_framework import serializers
from .models import Customer
from .models import *

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('pk','first_name', 'last_name', 'email', 'phone','address','description')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'


class TeacherSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    phone=serializers.IntegerField()
    group=GroupSerializer()
