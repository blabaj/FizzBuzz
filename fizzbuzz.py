# -*- coding: utf-8 -*-

poskusi = False
while poskusi != True:
    vnos = raw_input("Vnesi število: ")
    try:
        vnos = int(vnos)
        poskusi = True
    except ValueError:
        print "Kar si vnesel ni število, poskusi ponovno!"

for x in range (1, vnos+1):
    preveris3 = x % 3
    preveris5 = x % 5
    if (preveris3 == 0 and preveris5 == 0):
        print "fizzbuzz"
    elif (preveris3 == 0 and preveris5 != 0):
        print "fizz"
    elif (preveris3 != 0 and preveris5 == 0):
        print "buzz"
    else:
        print x