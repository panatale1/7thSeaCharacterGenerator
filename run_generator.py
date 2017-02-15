from source_select import select_sources
from generator import character_generator

from nationalities import core_nationalities
from backgrounds import core_backgrounds
from advantages import core_advantages
from arcana import core_arcana
from sorceries import core_sorceries
from dueling import core_dueling

SOURCES = []


select_sources()
nationality_list = ["Choose One"]
for item in core_nationalities:
    nationality_list.append(item['nationality'])
if 'Heroes and Villains' in SOURCES:
    from backgrounds import hv_backgrounds
    from advantages import hv_advantages
if 'Pirate Nations' in SOURCES:
    from nationalities import pirate_nationalities
    for item in pirate_nationalities:
        nationality_list.append(item['nationality'])
    from backgrounds import pirate_backgrounds
    from advantages import pirate_advantages
    from arcana import pirate_arcana
    from sorceries import hv_sorceries
    from dueling import pirate_dueling
character_generator()
