import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from resources.datatables import FactionStatus
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('crackdown_imperial_colonel_hard')
	mobileTemplate.setLevel(88)
	mobileTemplate.setDifficulty(Difficulty.ELITE)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("rebel")
	mobileTemplate.setAssistRange(6)
	mobileTemplate.setStalker(False)
	mobileTemplate.setFaction("rebel")
	mobileTemplate.setFactionStatus(FactionStatus.Combatant)
	mobileTemplate.setOptionsBitmask(Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_rebel_lieutenant_colonel_human_male_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_lieutenant_colonel_human_male_02.iff')
	templates.add('object/mobile/shared_dressed_rebel_lieutenant_colonel_moncal_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_lieutenant_colonel_rodian_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_lieutenant_colonel_rodian_male_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_lieutenant_colonel_zabrak_male_01.iff')			
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/carbine/shared_carbine_e5.iff', WeaponType.CARBINE, 1.0, 15, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('decorated_rebel_colonel_88', mobileTemplate)
	return