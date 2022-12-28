#!/usr/bin/python3
import uuid
import datetime
"""BaseModel module that contains a class that defines
all common attributes/methods for
other classes.
"""


class BaseModel():
    """BaseModel class that defines all common attributes/methods for
    other classes.
    """
    def __init__(self):
        """Init method
        sets an instance id and the time attrivutes to the current time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """sets the format for printing a BaseModel object

        Returns:
            _A string
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves the object to a JSON file
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dict withb the values of the __dict__ attribute
        of the object afer adding a __class__ key and converting the
        times to ISOformat

        Returns:
            _dict_: the object dict
        """
        my_dict = self.__dict__
        my_dict['__class__'] = type(self).__name__
        self.created_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return my_dict


# test = BaseModel()
# print(test.to_dict())
