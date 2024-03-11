#!/usr/bin/python3
"""This module creates a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Managing city objects
    Attributes:
        state_id (str): the state id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
