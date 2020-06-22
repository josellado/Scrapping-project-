
import pandas as pd
import numpy as np

army= pd.read_csv("output/army_Clean.csv") 


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


if __name__ == '__main__':
    print(main())