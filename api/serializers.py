from app.models import *
from rest_framework import serializers

class Bankserializers(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields='__all__'

class Branchserializers(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'