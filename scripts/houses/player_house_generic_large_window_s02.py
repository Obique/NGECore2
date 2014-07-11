import sys
from services.housing import HouseTemplate
from engine.resources.scene import Point3D

def setup(housingTemplates):
	houseTemplate = HouseTemplate("object/tangible/deed/player_house_deed/shared_generic_house_large_window_s02_deed.iff", "object/building/player/shared_player_house_generic_large_window_s02.iff", 2)
	
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(float(10.4), float(3), float(-11)))
	houseTemplate.addPlaceablePlanet("tatooine")
	houseTemplate.addPlaceablePlanet("corellia")
	houseTemplate.addPlaceablePlanet("naboo")
	houseTemplate.addPlaceablePlanet("talus")
	houseTemplate.addPlaceablePlanet("rori")
	houseTemplate.addPlaceablePlanet("dantooine")
	houseTemplate.addPlaceablePlanet("lok")
	houseTemplate.setDefaultItemLimit(500)
	houseTemplate.setDestructionFee(2500)
	houseTemplate.setBaseMaintenanceRate(26)
	
	housingTemplates.put(houseTemplate.getDeedTemplate(), houseTemplate)
	return