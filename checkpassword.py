#! /usr/bin/python
print "Created by Cory Noll (Null) Crimmins - Golden on May 12 2018 6:41 AM"
print "Voyant assignment #1"
print "MIT License"

import sys

argLength = len(sys.argv)-1 # We don't care about the script location
script = sys.argv[0] # That last line was a lie... we do...

if argLength == 0:
    print "Expected:"
    print "$ " + script + " foo"
    print "Not common password"
else:
    # Cheap HACK: Adding \n to password so I don't have to do anything on the list
    #"football" != "football\n"
    password = sys.argv[1] + "\n"
    file = open("1000MostCommonPasswords(byDavidWittman).txt", "r")
    commonPasswords = file.readlines()
    file.close()
    match = 0
    for item in commonPasswords:
        if password == item:
            match = 1
            break
    if match == 1:
        print "Common password"
    else:
        print "Not common password"
