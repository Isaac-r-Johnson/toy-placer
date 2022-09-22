run = True
placed = False
cor = [None, None, None]
headings = ["north", "east", "south", "west"]
MOVE = "move"
LEFT = "left"
RIGHT = "right"
PLACE = "place"
REPORT = "report"

while run:
    command = input("Enter command: ")
    command = command.lower()

    if command[0:5] == PLACE:
        try:
            __none, pos = command.split(" ")
            x, y, h = pos.split(",")
            x = int(x)
            y = int(y)
        except ValueError:
            print("Please type command correctly!")
            continue
        if x <= 5:
            if x >= 0:
                if y <= 5:
                    if y >= 0:
                        if h in headings:
                            cor[0] = x
                            cor[1] = y
                            cor[2] = h
                            placed = True
                        else:
                            print("Please type command correctly!")
                    else:
                        print("Please type command correctly!")
                else:
                    print("Please type command correctly!")
            else:
                print("Please type command correctly!")
        else:
            print("Please type command correctly!")
    elif command == MOVE and placed:
        if cor[2] == headings[0] and cor[1] < 5:
            cor[1] += 1
        elif cor[2] == headings[1] and cor[0] < 5:
            cor[0] += 1
        elif cor[2] == headings[2] and cor[1] > 0:
            cor[1] -= 1
        elif cor[2] == headings[3] and cor[0] > 0:
            cor[0] -= 1
        else:
            print("Sorry, you are trying to move the toy out of bounds")
    elif command == LEFT and placed:
        if cor[2] == headings[0]:
            cor[2] = headings[3]
        elif cor[2] == headings[1]:
            cor[2] = headings[0]
        elif cor[2] == headings[2]:
            cor[2] = headings[1]
        elif cor[2] == headings[3]:
            cor[2] = headings[2]
    elif command == RIGHT and placed:
        if cor[2] == headings[0]:
            cor[2] = headings[1]
        elif cor[2] == headings[1]:
            cor[2] = headings[2]
        elif cor[2] == headings[2]:
            cor[2] = headings[3]
        elif cor[2] == headings[3]:
            cor[2] = headings[0]
    elif command == REPORT and placed:
        if placed:
            print(f"Toy is placed at {cor[0]},{cor[1]} facing {cor[2]}")
    else:
        print("Command not found: " + command)
