#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, breed="Mastiff", name="name"):
        self.breed = breed
        self.name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if not isinstance(value, str) or not 1 <= len(value) <= 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value
    
    def get_breed(self):
        return self._breed
    
    def set_breed(self, value):
        if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value
    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
