from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.


class NigeriaLGA(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=75)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=75)
    varname_2 = models.CharField(max_length=150)
    nl_name_2 = models.CharField(max_length=75)
    hasc_2 = models.CharField(max_length=15)
    cc_2 = models.CharField(max_length=15)
    type_2 = models.CharField(max_length=50)
    engtype_2 = models.CharField(max_length=50)
    validfr_2 = models.CharField(max_length=25)
    validto_2 = models.CharField(max_length=25)
    remarks_2 = models.CharField(max_length=100)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __repr__(self):
    	return '<NigeriaLGA: %s %s>' % (self.name_2,self.name_1)

    @property
    def state(self):
        return self.name_1

    @property
    def lga(self):
        return self.name_2
    

    def __str__(self):
    	return self.name_2

