#!/bin/python3

from sys import argv
from Classes import *


def get_args():
    if len(argv) != 2:
        print("Not the input we expected")
        exit(1)
    try:
        with open(argv[1], "r") as f:
            line1 = f.readline().rstrip().split(" ")
            # D = duration
            # I = nb Intersection
            # S = nb Streets
            # V = nb cars
            # F = feed points if the car reaches it's destination on time.
            D, I, S, V, F = list(map(int, line1))
            _ = F
            _ = D
            streets = []
            intersections = [Intersection(i) for i in range(I)]
            cars = []
            _ = cars
            for i in range(S):
                _ = i
                line = f.readline().rstrip().split(" ")
                name = line.pop(2)
                B, E, L = list(map(int, line))
                street = Street(name, B, E, L)
                streets += [street]
                intersections[B].ostreets += [street]
                intersections[E].istreets += [street]

            for i in range(V):
                line = f.readline().rstrip().split(" ")
                P = int(line.pop(0))
                path = line
                cars += [Car(P, path)]
        return streets, intersections, cars
    except:
        print("Woops something went wrong")
        exit(1)


if __name__ == '__main__':
    streets, intersections, cars = get_args()
