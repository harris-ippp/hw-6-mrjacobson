#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


header = pd.read_csv("president_general_" + str(1924) +".csv", nrows = 1).dropna(axis = 1)
d = header.iloc[0].to_dict()

df = pd.read_csv("president_general_" + str(1924) +".csv", index_col = 0,
                 thousands = ",", skiprows = [1])

df.rename(inplace = True, columns = d) # rename to democrat/republican
df.dropna(inplace = True, axis = 1)    # drop empty columns
df["Year"] = 1924
allyears = df

for year in range(1928,2020,4):
    header = pd.read_csv("president_general_" + str(year) +".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv("president_general_" + str(year) +".csv", index_col = 0,
                     thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year
    colnames = df.columns.values
    keeplist = ["Democratic", "Republican", "Total Votes Cast", "Year"]
    for name in colnames:
        if name not in keeplist:
            if name not in df.columns.values: continue
            df = df.drop(name, 1)

    allyears = pd.concat([allyears, df])

allyears['index1'] = allyears.index

allyears["Republican Share"] = allyears["Republican"]/allyears["Total Votes Cast"]
allyears = allyears.drop(["All Others", "Progressive"], 1)
for county in ["Accomack County", "Albemarle County",
               "Alexandria City", "Alleghany County"]:
    mask = allyears["index1"] == county
    plt.plot(allyears[mask]["Year"], allyears[mask]["Republican Share"])
    plt.xlabel("Year")
    plt.ylabel("Republican Vote Share")
    plt.title(county)
    plt.savefig(county + ".pdf", format = "pdf")
#    plt.show()
