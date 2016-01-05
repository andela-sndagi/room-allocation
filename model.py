"""
    Model for the rooms at the building (Amity)
"""
class Room(object):
    """Room represents a Room in the building"""
    def __init__(self, name): #It has to have a name
        self.name = name

class Office(Room):
    """Office is a Room (inherits from Room)"""
    def __init__(self, name):
        super(Office, self).__init__(name) #Room initialize with its Room.__init__

class LivingSpace(Room):
    """LivingSpace is a Room"""
    def __init__(self, name):
        super(LivingSpace, self).__init__(name) ##Room initialize with its Room.__init__


"""
    Model for the employees at Amity
"""
class Person(object):
    """Person represents an employee (Fellow and Staff)"""
    def __init__(self, name): #Every person has a name
        self.name = name
        self.is_allocated_office = False

class Staff(Person):
    """Staff is a Person"""
    def __init__(self):
        super(Staff, self).__init__()

class Fellow(Person):
    """Fellow is a Person"""
    def __init__(self, is_interested): #Either Y or N (to be read from file)
        super(Fellow, self).__init__()
        self.is_interested = is_interested
