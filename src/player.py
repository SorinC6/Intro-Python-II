# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)

    def getItems(self):
        return [value for value in self.items]

    def __str__(self):
        items_format = [value for value in self.items]
        return f"Palyer: {self.name}, {self.current_room},Player Items: {items_format}"
