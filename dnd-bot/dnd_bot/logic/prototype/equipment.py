import copy

from dnd_bot.database.database_equipment import DatabaseEquipment
from dnd_bot.logic.prototype.database_object import DatabaseObject
from dnd_bot.logic.prototype.item import Item


class Equipment(DatabaseObject):
    """represents the player's equipped items"""
    def __init__(self, id_equipment: int = 1, helmet: Item = None, chest: Item = None, leg_armor: Item = None,
                 boots: Item = None, left_hand: Item = None, right_hand: Item = None, item_list=None,
                 accessory: Item = None):
        ## TODO super().__init__()
        if item_list is None:
            item_list = []
        self.id = id_equipment
        self.helmet = helmet
        self.chest = chest
        self.leg_armor = leg_armor
        self.boots = boots
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.accessory = accessory
