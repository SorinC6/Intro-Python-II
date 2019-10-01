# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        items_format = []
        if(self.items):
            items_format.append(self.items)
        else:
            items_format: "No items in the room"

        return f"Room: {self.name}, About: {self.description}, Items: {items_format}"
