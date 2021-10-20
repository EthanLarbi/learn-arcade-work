class Room:
    """
    This is a class that represents the player character
    """
    def __init__(self, name, north, east, west, south):
        """This is a method that sets up the variables in the object"""
        self.name = name
        self.north = north
        self.west = west
        self.east = east
        self.south = south



def main():
    print("Welcome to the Infamous Cottage Grove House!")
    room_list = []
    room = 0
    # This creates the address
    my_room = Room("This is the Entrance. There are stairs to the south of you, and the living room\n"
                   "to the west of you.", None, None, 1, 5)
    room_list.append(my_room)

    # This creates the address
    my_room = Room("You are in the living room. There is a dining room to the south of you,\n"
                   "and a the entrance to the east of you.", None, 0, None, 2)
    room_list.append(my_room)

    # This creates the address
    my_room = Room("You are in the dining room. There is a living room to the north, a bathroom to the west\n"
                   ", and a kitchen to the south.",  1, None, 3, 2)
    room_list.append(my_room)

    # This creates the address
    my_room = Room("You are in the bathroom. There is a dining room to the east of you.",  0, 2, None, None)
    room_list.append(my_room)

    # This creates the address
    my_room = Room("You are in the kitchen. There is a dinning room to the north of you.", 2, 2, None, None)
    room_list.append(my_room)

    # This creates the address
    my_room = Room("You are at the stairs. There is a bedroom to the south of you.", 0, None, None, 6)
    room_list.append(my_room)

    # This creates the address
    my_room = Room("This is the bedroom.There is a patio to the south, and the stairs are to the east of you.",  5, None, None, 8)
    room_list.append(my_room)

    # This creates the address
    my_room = Room("This is the garage. There is a patio to the north of you.", 7, None, None, None)
    room_list.append(my_room)

    my_room = Room("This is the patio. There is a garage to the south of you, and a bedroom to the north.\n"
                   "", 6, None, None, 7)
    room_list.append(my_room)

    done = False

    while not done:
        print()
        print(room_list[room].name)
        userinput = input("Where do you desire to go? ")

        if userinput.lower() == "q" or userinput.lower() == "quit":
            print("Thank you for attempting!")
            break

        if userinput.lower() == "n" or userinput.lower() == "north":
            next_room = room_list[room].north
            if next_room is None:
                print()
                print("There is nothing there.")
            else:
                room = next_room

        if userinput.lower() == "w" or userinput.lower() == "west":
            next_room = room_list[room].west
            if next_room is None:
                print("There is nothing there.")
            else:
                room = next_room

        if userinput.lower() == "e" or userinput.lower() == "east":
            next_room = room_list[room].east
            if next_room is None:
                print("There is nothing there.")
            else:
                room = next_room

        if userinput.lower() == "s" or userinput.lower() == "south":
            next_room = room_list[room].south
            if next_room is None:
                print("There is nothing there.")
            else:
                room = next_room


main()
