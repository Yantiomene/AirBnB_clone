#!/usr/bin/python3
"""
module that creates
users using inherited Basemodel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user inherited from basemodel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Create users"""
        super().__init__(self, *args, **kwargs)
