#!/bin/python3

class Street:
    def __init__(self, name, source, destination, time):
        self.name = name
        self.src = source
        self.dest = destination
        self.time = time


# class TrafficLight:
#     def __init__(self, initial_state):
#         self.state = initial_state


class Car:
    def __init__(self, n, path):
        self.n = n
        self.path = path


class Intersection:
    def __init__(self, ID):
        self.id = ID
        self.istreets = []
        self.ostreets = []
        self.open_street = 0
