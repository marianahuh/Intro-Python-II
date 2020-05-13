# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        str = f'{self.room} {self.description}'
        return str
