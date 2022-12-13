
#!/usr/bin/python3
""" main function test """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(62, 18, 7, 9)
    r2 = Rectangle(8, 7)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
