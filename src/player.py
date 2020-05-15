# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        # returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(f'\nYour current location is == {self.current_room.name}')
            print(self.current_room.description)
        else:
            print("YOU MAY NOT ENTER! Try a different direction.")
