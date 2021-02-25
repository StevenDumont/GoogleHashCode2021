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
    debug = False
    if debug:
        for street in streets:
            print("Street: " + street.name)
        for intersection in intersections:
            print("Intersection: " + str(intersection.id) +
                  " " + str(intersection.open_street))
        for car in cars:
            print("Car path: " + str(car.path))

    frequencies = {}
    for c in cars:
        for p in c.path:
            if not p in frequencies.keys():
                frequencies[p] = 0
            else:
                frequencies[p] += 1

    for inter in intersections:
        inter.weights = [1] * len(inter.istreets)
        # for i, street in enumerate(inter.istreets):
        #     if street.name in frequencies.keys():
        #         inter.weights[i] = frequencies[street.name]
        #     else:
        #         inter.weights[i] = 0
        # 
        # if all(v == 0 for v in inter.weights) or len(inter.istreets) == 0:
        #     inter.weights = [1] * len(inter.istreets)
        #     continue
        # 
        # m = min([v for v in inter.weights if v != 0])
        # for i, w in enumerate(inter.weights):
        #     inter.weights[i] = min(round(w / m), 2)

    print(len([i for i in intersections if any(w != 0 for w in i.weights)]))
    for inter in intersections:
        print(inter.id)
        print(len([w for w in inter.weights if w != 0]))
        for street, weight in zip(inter.istreets, inter.weights):
            if weight:
                print(street.name, weight)
