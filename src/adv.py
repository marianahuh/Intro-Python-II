from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# Items in rooms

candle = Item('candle', 'To light your path.')
compass = Item('compass', 'When you lose your way.')
cloak = Item('cloak', 'To take the chill off.')

room['foyer'].items = ['candle']
room['overlook'].items = ['compass']
room['narrow'].items = ['cloak']

# collection
collection = []


def itemsInRoom(c, current_room):
    attr = c + '_to'

    if hasattr(current_room, attr):
        return getattr(current_room, attr)

    return current_room


# Make a new player object that is currently in the 'outside' room.
player = Player(input('\nEnter your username: '), room['outside'])
print(f'Welcome, {player.name}!\n')
print(f'You start your quest here == {player.current_room.name}\n')
print(f'###  {player.current_room.description}  ###')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
while True:
    action = input(
        "\nMake a move: (n)orth (s)outh (e)ast (w)est (c)ollection (d)rop (q)uit > ")
    if action in ('n', 's', 'e', 'w'):
        player.move(action)
        # If the user enters "q", quit the game.
    elif action == 'q':
        print('\nThank you for playing! Farewell!\n')
        exit()
    print(
        f'\nYou found a {player.current_room.items} in the {player.current_room.name}!\n')
    if len(player.current_room.items) > 0:
        pick_up = input(
            f'Do you want to take the {player.current_room.items}? (y)es or (n)o: ')
        if pick_up == 'y':
            collection.append(player.current_room.items)
            player.current_room.items = []
            print(collection)

    elif action == 'c':
        player.collection()
    elif action[0] == 'y':
        index = 0
        for c in collection:
            index += 1
            print(f'{index}.{c}')
        if len(collection) == 0:
            print('There is nothing in your collection')

    elif action[0] == 'd':
        index = 0
        for c in collection:
            index += 1
            print(f'{index}.{c}')
        remove = input(
            'Which item do you wish to leave behind? 1, 2, or 3? \n')
        collection.remove(collection[int(remove)-1])
    else:
        # Print an error message if the movement isn't allowed.
        print("\n=== Not a valid move. Please enter: n, s, e, w or q to Quit")
        # If the user enters a cardinal direction, attempt to move to the room there.
