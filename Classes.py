#!/bin/python3

class Street:
    def __init__(self, name, source, destination, time):
        self.name = name
        self.src = source
        self.dest = destination
        self.time = time

class Intersection:
    def __init__(self, ID, streets):
        self.ID = ID
        self.streets = streets
        self.open_street = 0
