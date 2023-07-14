#!/usr/bin/python3
"""
Inherited Review Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inheriting from basemodel
    Public class attributes:
    place_id: string - empty string
    user_id: string - empty string
    text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
