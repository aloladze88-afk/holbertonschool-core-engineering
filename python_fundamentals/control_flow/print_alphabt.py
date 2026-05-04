#!/usr/bin/env python3
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != "q" and letter != "e":
        print("{}".format(letter), end="" if letter != "z" else "\n")
        