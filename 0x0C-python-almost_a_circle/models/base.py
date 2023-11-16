#!/usr/bin/python3
"""A Base class module
"""
import json


class Base:
    """A base class.

    :param id: id of a ``Base`` instance
    :type id: int
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation.

        :param list_dictionaries: a list of dictionaries
        :type list_dictionaries: list
        :return: JSON string representation of list of dictionaries
        :rtype: str
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON representation of list of objects to a file.

        :param list_objs: list of instances who inherits of Base class
        :type list_objs: list
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as fp:
            if list_objs is None:
                fp.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                data = cls.to_json_string(list_dict)
                fp.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list from the JSON string representatio.

        :param json_string: a JSON string representation
        :type json_string: str
        :return: the list of dict used to create the JSON string
        :rtype: list
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        :param dictionary: a dictionary of attribute/value of the instance
        :type dictionary: dict
        :return: a new instance with the attributes values set from
                 the dictionary
        :rtype: object
        """
        if cls.__name__ == "Base":
            return cls()
        else:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)

            dummy.update(**dictionary)
            return dummy
