#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

addr = "http://historical.elections.virginia.gov/elections/search/year_from:\
    1924/year_to:2016/office_id:1/stage:General"

resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")
elections = soup.find_all("tr", attrs={"election_item general_party"})
elec = []
for i in range(len(elections)):
    temp = elections[i].attrs['id']
    electionid = temp.split("-")[2]
    year = elections[i].td.string
    elec.append(year + " " + electionid)


output = open("ELECTION_ID", "w")

for line in elec:
    output.write(line + '\n')
output.close()
