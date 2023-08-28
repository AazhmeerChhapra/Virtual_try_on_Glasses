
from rest_framework import serializers 
from store.models.FielsToBeSent import FieldsToBeSent

class FieldsToBeSentSerializers (serializers.ModelSerializer):
    class Meta:
        model=FieldsToBeSent
        fields=['id','number']