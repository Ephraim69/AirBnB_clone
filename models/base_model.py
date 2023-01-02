#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel module that contains a class that defines
all common attributes/methods for
other classes.
"""


class BaseModel():
    """BaseModel class that defines all common attributes/methods for
    other classes.
    """
    def __init__(self, *args, **kwargs):
        """Init method
        sets an instance id and the time attrivutes to the current time
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                elif key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
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
        self.updated_at = datetime.now()

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
