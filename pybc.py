#!/bin/python

# Name:         Python Number Base Converter
# Author:       Alek Mugnozzo
# Version:      1.0.0
# E-mail:       info@mugnozzo.net
# Website:      mugnozzo.net
# License:      GNU GPLv3.0
# Hosted at:    https://github.com/mugnozzo/python-number-base-converter

import argparse
from configparser import ConfigParser # to parse config.ini
import os.path # to check config file and input file

path=os.path.dirname(os.path.realpath(__file__))
confPath=path+"/config.ini"

# Looking for config.ini
config=None
if os.path.exists(confPath):
    config=ConfigParser()
    config.read(confPath)
else:
    raise Exception("File config.ini not found in directory "+path+". Did you copy/move config.def.ini to config.ini?")

alphabets=config["Alphabets"]

aSou=alphabets['source_alphabet']
aDes=alphabets['destination_alphabet']

argParser=argparse.ArgumentParser()
argParser.add_argument("-n","--number",help="number to convert",required=True)
argParser.add_argument("-s","--source-base",help="source base",required=True)
argParser.add_argument("-d","--destination-base",help="destination base",required=True)

args = argParser.parse_args()

n=args.number
s=int(args.source_base)
d=int(args.destination_base)

if aSou=="ASCII":
    aSou=""
    for i in range(32,127):
        aSou+=chr(i)
if aDes=="ASCII":
    aDes=""
    for i in range(32,127):
        aDes+=chr(i)

if len(aSou)<s:
    raise Exception("The source alphabet has "+str(len(aSou))+" elements, that is less than "+str(s)+" (the source base).")

for ch in aSou:
    if aSou.count(ch)!=1:
        raise Exception("The source alphabet contains duplicate characters.")

for ch in aDes:
    if aDes.count(ch)!=1:
        raise Exception("The destination alphabet contains duplicate characters.")

for ch in n:
    if aSou[0:s].count(ch)!=1:
        if aSou.count(ch)!=1:
            raise Exception("Character "+ch+" is not in source alphabet.")
        raise Exception("Character "+ch+" is out of range.\nSource alphabet trimmed to base "+str(s)+" is "+str(aSou[0:s]))

n10=0
i=0
for c in n:
    ind=aSou.index(c)
    n10+=aSou.index(c)*(s**(len(n)-1-i))
    i+=1

nd=""
while(n10!=0):
    nd+=aDes[n10%d]
    n10=int(n10/d)

print("Base "+str(s)+": "+str(n))
print("Base "+str(d)+": "+nd[::-1])

