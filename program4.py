import math

def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

while True:
    print("\nCALCULATIONS MENU")
    print("1) AREA (SQUARE)")
    print("2) AREA (RECTANGLE)")
    print("3) AREA (CIRCLE)")
    print("4) PERIMETER (SQUARE)")
    print("5) PERIMETER (RECTANGLE)")
    print("6) PERIMETER (CIRCLE)")
    print("7) EXIT THE PROGRAM")
    choice = input("INPUT MENU CHOICE (1, 2, 3, 4, 5, 6 or 7)? ")

    if choice == "1":
        side = float(input("INPUT SIDE LENGTH? "))
        area = square_area(side)
        print("AREA IS", area)

    elif choice == "2":
        length = float(input("INPUT LENGTH? "))
        width = float(input("INPUT WIDTH? "))
        area = rectangle_area(length, width)
        print("AREA IS", area)

    elif choice == "3":
        radius = float(input("INPUT RADIUS? "))
        area = circle_area(radius)
        print("AREA IS", area)

    elif choice == "4":
        side = float(input("INPUT SIDE LENGTH? "))
        perimeter = square_perimeter(side)
        print("PERIMETER IS", perimeter)

    elif choice == "5":
        length = float(input("INPUT LENGTH? "))
        width = float(input("INPUT WIDTH? "))
        perimeter = rectangle_perimeter(length, width)
        print("PERIMETER IS", perimeter)

    elif choice == "6":
        radius = float(input("INPUT RADIUS? "))
        perimeter = circle_perimeter(radius)
        print("PERIMETER IS", perimeter)

    elif choice == "7":
        print("EXITING, THE AUTHOR, MESHAAL M. KHAN, WOULD LIKE TO WISH YOU A WONDERFUL DAY")
        break

    else:
        print("I NEED YOU TO READ THE CALCULATIONS MENU, AND CHOOSE A NUMBER FROM 1-7. THANK YOU")
