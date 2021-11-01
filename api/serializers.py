from rest_framework import serializers
from .models import api

class apiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api
        fields = ('id','name','isbn','authors','number_of_pages','publisher','country','release_date')