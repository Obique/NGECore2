import sys

def setup(core, actor, buff):
	core.buffService.addBuffToCreature(actor, 'bh_armor_sprint_1')
	return
	
def run(core, actor, target, commandString):
	return