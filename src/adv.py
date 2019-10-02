from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [Item("fists", "First Weapon")],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [Item("torch", "the faint glow from this torch can light up a room")],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [Item("shiled", "protection from fire")],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [Item("sword", "Best weapon for close attack")],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [Item("fork", "without description")],
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_creation = input("Enter a player name: ")

initial_room = room["outside"]
player = Player(player_creation, initial_room)
print(f"******Player Info*********\n{player}\n\n")

user_choice = ""

# Write a loop that:
#
while user_choice != "q":
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print("****** Current Room *******\n" + player.current_room.name)
    print(player.current_room.description + "\n\n")

    # * Waits for user input and decides what to do.
    user_direction = input(
        "Choose a direction: (n)-Nord , (e)-East , (s)-South, (w)-West "
    )
    user_choice = user_direction
    parse = user_direction.split(" ")

    # If the user enters a cardinal direction, attempt to move to the room there.
    if len(parse) == 1:
        if (
            user_direction == "n"
            or user_direction == "e"
            or user_direction == "s"
            or user_direction == "w"
        ):
            # print(
            # f"Player Direction: {user_direction} Player Location: {player.current_room}")
            new_direction = f"{user_direction}_to"
            # print(f"New Direction: {new_direction}")
            if hasattr(player.current_room, new_direction):
                player.current_room = getattr(player.current_room, new_direction)
                cc = player.current_room.name.split(" ")
                if len(cc) == 2:
                    cc = cc[1]
                else:
                    cc = cc[0]
                print(
                    f"New Dirrection: {player.name} in going to {user_direction} in {player.current_room.name}"
                )
                print("********Current Item in the room***** " + cc.lower())

                print(room[cc.lower()].getItem())

            else:
                print(f"You hit a wall, keep trying")
        elif user_direction == "i":
            if len(player.items) > 0:
                print(f"{player.name} items are: {player.items}")
            else:
                print(f"{player.name} does't have any items in inventory")
        elif user_direction == "q":
            print("Game Over")
        else:
            print("Invalid input")
    if len(parse) == 2:

        if parse[0] == "get":
            pass
            # Print an error message if the movement isn't allowed.
            #
            # If the user enters "q", quit the game.
