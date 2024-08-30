#!/usr/bin/env python3

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    

    def __init__(self, name="brian", breed=""):
        self.name = None
        self.breed = None
        self._set_name(name)
        self._set_breed(breed)

    def _set_name(self, name):
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

    def _set_breed(self, breed):
        if breed and breed not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
        elif breed:
            self.breed = breed
