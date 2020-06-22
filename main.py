#!/usr/bin/env python3

from argparse import ArgumentParser
import pandas as pd
from src import functions
from functools import reduce


army= pd.read_csv("output/army_Clean.csv") 

parser = ArgumentParser(description="Este programa es para que Dumbledore conozca la fuerza que posee en cada asociacion y los magos que podria reclutar")

parser.add_argument( "-m", "--ministryOfMagic", help="Que aliados tiene dumbledore en el ministerio", action ='store_true')
parser.add_argument( "-p", "--orderOfThePhenix",help="Cuales son los Miembros de la orden", action="store_true")
parser.add_argument("-d", "--dumbledoresArmy", help="Aliados ya en el ejercito", action="store_true")
args = parser.parse_args()
print (args)


def main():
    army= pd.read_csv("output/army_Clean.csv")
    select = []
    if args.ministryOfMagic: 
        select.append(army['ministryOfMagic'])
    if args.orderOfThePhenix: 
        select.append(army['orderOfThePhoenix'])   
    if args.dumbledoresArmy: 
        select.append(army['dumbledoresArmy']) 
    if not select: 
        return army
    else:
        select = reduce(lambda a,b: a | b, select)
    return army[select]
if __name__ =="__main__":
    print(main())