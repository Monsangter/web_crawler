from rest_framework import serializers
from .models import Wanted, Jobkorea, Saramin

class WantedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wanted
        fields = '__all__'

class JobkoreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobkorea
        fields = '__all__'

class SaraminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saramin
        fields = '__all__'