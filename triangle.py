#!/usr/bin/env python3

# For loop triangle
STAR = 9
for i in range(0, STAR):
    for j in range(i):
        print("*", end='')
    print()
print()
# For Loop for reverse triangel
for i in range(STAR, 0, -1):
    for j in range(i):
        print("*", end='')
    print("")
print()
# For Loop for opposite triangle
for i in range(STAR, 0, -1):
    for j in range(i):
        print(" ", end='')
    for k in range(STAR-j):
        print ("*", end='')
    print()
print()
# For loop for pyrimid
for i in range(STAR, 0, -1):
    for j in range(i):
        if(j % 2 == 0):
            print(" ", end='')
    for k in range(STAR-j):
        if(i % 2 != 0):
            print("*", end='')
    if(j % 2 != 0):
        print()
print()
print()
# For loop for inverted pyrimid
for i in range(STAR, 0, -1):
    for j in range(i):
        if(j % 2 == 0):
            print("*", end='')
    if(j % 2 != 0):
        print()
print()
print()
# For loop for inverted pyrimid
for i in range(STAR, 0, -1):
    # print(i, end='')
    for j in range(i):
        if(j % 2 == 0):
            print("*", end='')
    if(j % 2 != 0):
        print("")
    if (i % 2 == 0):
        for k in range(STAR, i, -2):
            print(" ", end='')
print()
# For loop for kite
