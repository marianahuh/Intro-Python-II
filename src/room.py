# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # define an init method to the constructor and add attributes to the base class object
    def __init__(self, name, description):  # take values as parameters and
        self.name = name                              # assign to the attributes
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):  # str method returns the string representation of the object
        return_str = self.name
        return_str = self.description
        return return_str
