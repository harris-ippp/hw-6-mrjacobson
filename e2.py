#!/usr/bin/env python

import requests


for line in open("ELECTION_ID", "r"):
    elecid = line[-6:-1]
    year = line[:4]
    resp = requests.get("http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(elecid))
    file_name = "president_general_" + year +".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
