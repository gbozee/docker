# -*- coding: utf-8 -*-

import os
from django.contrib.gis.utils import LayerMapping 
from world.models import WorldBorder
import world

world_mappings = {
	'fips': 'FIPS',
	'iso2': 'ISO2',
	'iso3': 'ISO3',
	'un':'UN',	
	'name':'NAME',
	'area':'AREA',
	'pop2005':'POP2005',
	'region':'REGION',
	'subregion':'SUBREGION',
	'lon':'LON',
	'lat':'LAT',
	'mpoly':'MULTIPOLYGON'
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(world.__file__),'data','TM_WORLD_BORDERS-0.3.shp'))

def run(verbose=True):
	lm = LayerMapping(WorldBorder,world_shp,world_mappings,
		transform=False,encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)