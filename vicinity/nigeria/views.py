from django.shortcuts import render
from .models import NigeriaLGA
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import viewsets,serializers
# Create your views here.

class NigeriaLGASerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = NigeriaLGA
		fields = ('lga','state')


# ViewSets define the view behavior.
class NigeriaLGAViewSet(viewsets.ModelViewSet):
    queryset = NigeriaLGA.objects.all()
    serializer_class = NigeriaLGASerializer

    def get_queryset(self):
    	queryset = NigeriaLGA.objects.all()
    	latitude = self.request.query_params.get('latitude', None)
    	longitude = self.request.query_params.get('longitude', None)
    	if latitude and longitude:
    		pnt = 'POINT(%s %s)' % (longitude,latitude)
    		queryset = queryset.filter(geom__contains=pnt)
    	return queryset