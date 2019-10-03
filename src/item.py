# class to hold item information


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_drop(self):
        return f"Nooo! You just dropped {self.name}"

    def on_take(self):
        return f"Bravo! You just picked {self.name} - {self.description}"

    def __str__(self):
        return f"Item Name: {self.name}, Description: {self.description}"
