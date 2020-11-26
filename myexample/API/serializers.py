
from rest_framework import serializers

from API.models import Sede, Stand


class StandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stand
        exclude = ('id',)

class SedeSerializer(serializers.ModelSerializer):

    #stands = StandSerializer(many=True)
    class Meta:
        model = Sede
        fields = ['nombre']
        #fields = ['nombre','stands']

