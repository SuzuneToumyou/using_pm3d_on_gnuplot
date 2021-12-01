#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import math
import pathlib as pl

p_temp = pl.Path(".").glob("*.csv")
for p in p_temp:

    with p.open() as f:
        reader=csv.reader(f)

        fout=open("./out/" + str(p) ,"a")

        ttmp=0

        for row in reader:
            
            if ttmp != row[0]:
                fout.write("\n" + row[0] + "," + row[1] + "," + row[2] + "\n")

            else :
                fout.write(row[0] + "," + row[1] + "," + row[2] + "\n")

            ttmp = row[0]

        
        fout.close()
        f.close()
