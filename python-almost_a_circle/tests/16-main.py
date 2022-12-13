#!/usr/bin/python3
""" main function test """
from models.rectangle import Rectangle

if __name__ == "__main__":
    list_input = [
	{'id': 50, 'width': 21, 'height': 5},
	{'id': 62, 'width': 5, 'height': 12}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))
