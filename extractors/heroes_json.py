import json
from pathlib import Path
from typing import List

from DataTypes import Ability, Hero

LOC_PATH_HEROES = "data/citadel_heroes_english.txt"
LOC_PATH_GC = "data/citadel_gc_english.txt"
ABILITIES_VDATA_PATH = "data/vdata/abilities.vdata.json"
HEROES_VDATA_PATH = "data/vdata/heroes.vdata.json"
STRINGMAP_PATH = "data/stringmap.json"

def extract_id_by_name(name: str) -> str:
    json_map = json.loads(Path(STRINGMAP_PATH).read_text())
    for id, str_name in json_map.items():
        if str_name == name:
            return id
    return "0"

def extract_localization_ability(ability: str) -> str:
    with open(f"./{LOC_PATH_HEROES}", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if ability in line:
                parts = line.strip().split("\"") 
                parts = list(filter(lambda x: x.strip() != "", parts))
                return parts[1]
    return ability

def extract_localization_hero(hero: str) -> str:
    with open(f"./{LOC_PATH_GC}", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if hero in line:
                parts = line.strip().split("\"") 
                parts = list(filter(lambda x: x.strip() != "", parts))
                return parts[1]
    return hero

def create_heroes_json():
    abilities_vdata = json.loads(Path("data/vdata/abilities.vdata.json").read_text())
    abilities: List[Ability] = []
    heroes: List[Hero] = []
    
    for ability in abilities_vdata["Root"]:
        ability_data = abilities_vdata["Root"][ability]
        if "m_strAbilityImage" in ability_data and \
            "hud/abilities" in ability_data["m_strAbilityImage"] and \
                "m_eAbilityType" in ability_data and \
                    (ability_data["m_eAbilityType"] == "EAbilityType_Ultimate" or ability_data["m_eAbilityType"] == "EAbilityType_Signature"):
            abilities.append({
                "id": int(extract_id_by_name(ability)),
                "name": ability,
                "image": ability_data["m_strAbilityImage"].replace("file://{images}/hud/abilities", "abilities").replace(".psd", ".png"),
                "localization": extract_localization_ability(ability),
            })
    
    heroes_vdata = json.loads(Path(HEROES_VDATA_PATH).read_text())
    for hero in heroes_vdata["Root"]:
        if not hero.startswith("hero_"): continue
        hero_data = heroes_vdata["Root"][hero]
        hero_abilities = [None] * 4
        for ability in hero_data["m_mapBoundAbilities"]:
            if ability.startswith("ESlot_Signature_"):
                ability_slot = ability.replace("ESlot_Signature_", "")
                ability_slot = int(ability_slot) - 1
                ability_name = hero_data["m_mapBoundAbilities"][ability]
                hero_abilities[ability_slot] = next((x for x in abilities if x["name"] == ability_name), None)
        hero_abilities = list(filter(lambda x: x is not None, hero_abilities))
        hero_image = ""
        if "m_strSelectionImage" in hero_data:
            hero_image = hero_data["m_strSelectionImage"].replace("file://{images}/heroes", "heroes").replace(".psd", ".png")
        elif "m_strIconHeroCard" in hero_data:
            hero_image = hero_data["m_strIconHeroCard"].replace("file://{images}/heroes", "heroes").replace(".psd", ".png").replace("_card", "")
        heroes.append({
            "id": hero_data["m_HeroID"],
            "name": hero,
            "localization": extract_localization_hero(hero),
            "image": hero_image,
            "abilities": hero_abilities
        })

    Path("data/heroes.json").write_text(json.dumps(heroes, indent=4))
