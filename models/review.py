#!/usr/bin/python3
'''review model class'''

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherit from BaseModel class
    """
    place_id = ""
    user_id = ""
    text = ""
