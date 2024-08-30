import json
from pathlib import Path
from typing import List

from DataTypes import Item, ItemType

LOC_PATH_GC = "data/citadel_gc_english.txt"
ITEMS_VDATA_PATH = "data/vdata/abilities.vdata.json"
STRINGMAP_PATH = "data/stringmap.json"

def extract_id_by_name(name: str) -> str:
    json_map = json.loads(Path(STRINGMAP_PATH).read_text())
    for id, str_name in json_map.items():
        if str_name == name:
            return id
    return "0"

def extract_localization_item(item: str) -> str:
    with open(f"./{LOC_PATH_GC}", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if item in line:
                parts = line.strip().split("\"") 
                parts = list(filter(lambda x: x.strip() != "", parts))
                return parts[1]
    return item

def create_items_json():
    items_vdata = json.loads(Path("data/vdata/abilities.vdata.json").read_text())
    items: List[Item] = []
    
    for item in items_vdata["Root"]:
        item_data = items_vdata["Root"][item]
        if "m_eItemSlotType" in item_data:
            item_type = item_data["m_eItemSlotType"]
            match item_type:
                case "EItemSlotType_Armor":
                    item_type = ItemType.ARMOR
                case "EItemSlotType_WeaponMod":
                    item_type = ItemType.WEAPON
                case "EItemSlotType_Tech":
                    item_type = ItemType.TECH
                case _: 
                    item_type = ItemType.TECH
            item_tier = int(item_data["m_iItemTier"].replace("EModTier_", "")) if "m_iItemTier" in item_data else 0
            item_image = ""
            if "m_strAbilityImage" in item_data:
                item_image = item_data["m_strAbilityImage"]
                item_image = item_image.replace("file://{images}/upgrades/", "items/")
                item_image = item_image.replace("file://{images}/hud/abilities/", "abilities/")
                item_image = item_image.replace(".psd", ".png")
            items.append({
                "id": int(extract_id_by_name(item)),
                "name": item,
                "localization": extract_localization_item(item),
                "tier": item_tier,
                "type": item_type,
                'image': item_image,
            })
    
    Path("data/items.json").write_text(json.dumps(items, indent=4))