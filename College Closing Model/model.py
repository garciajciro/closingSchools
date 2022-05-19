import csv
import pandas as pd
import matplotlib.pyplot as mp

dictclosed2022 = {}
dictclosed2021 = {}
dictclosed2020 = {}
dictclosed2019 = {}
cs1920 = {}
cs1819 = {}
cs1718 = {}
cs1617 = {}
cs1516 = {}
cs1415 = {}

# GET ALL OF THE SCHOOLS THAT CLOSED IN 2022, 2021, 2020, 2019
with open("closedschools/closedschools2022.csv") as close22:
    read = csv.reader(close22)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        dictclosed2022[row[1]] = row[2]

with open("closedschools/closedschools2021.csv") as close21:
    read = csv.reader(close21)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        dictclosed2021[row[1]] = row[2]


with open("closedschools/closedschools2020.csv") as close20:
    read = csv.reader(close20)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        dictclosed2020[row[1]] = row[2]

with open("closedschools/closedschools2019.csv") as close19:
    read = csv.reader(close19)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        dictclosed2019[row[1]] = row[2]
###########################################################################


# GET ALL OF THE COMPOSITVE SCORE FROM 2014 ALL THE WAY UNTIL 2020
with open("compositescores/cs1920.csv") as composite19:
    read = csv.reader(composite19)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        cs1920[row[0]] = [row[1], row[8]]

with open("compositescores/cs1819.csv") as composite18:
    read = csv.reader(composite18)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        cs1819[row[0]] = [row[1], row[8]]

with open("compositescores/cs1920.csv") as composite17:
    read = csv.reader(composite17)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        cs1718[row[0]] = [row[1], row[8]]

with open("compositescores/cs1920.csv") as composite16:
    read = csv.reader(composite16)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        cs1617[row[0]] = [row[1], row[8]]

with open("compositescores/cs1920.csv") as composite15:
    read = csv.reader(composite15)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        cs1516[row[0]] = [row[1], row[8]]

with open("compositescores/cs1920.csv") as composite14:
    read = csv.reader(composite14)
    for row in read:
        for x in range(len(row)):
            row[x] = row[x].strip()
        cs1415[row[0]] = [row[1], row[8]]
#######################################################################
schools19 = {}
schools18 = {}
schools17 = {}
schools16 = {}
schools15 = {}
schools14 = {}

nameOfColleges = []


# CREATE DICTIONARIES OF SCHOOLS THAT CLOSED IN EACH YEAR AND WHAT THEIR COMPOSITE SCORE IS
for x in dictclosed2022.keys():
    if x in cs1920:
        schools19[cs1920[x][0]] = cs1920[x][1]
        if cs1920[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1920[x][0])

    if x in cs1819:
        schools18[cs1819[x][0]] = cs1819[x][1]
        if cs1819[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1819[x][0])

    if x in cs1718:
        schools17[cs1718[x][0]] = cs1718[x][1]
        if cs1718[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1718[x][0])

    if x in cs1617:
        schools16[cs1617[x][0]] = cs1617[x][1]
        if cs1617[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1617[x][0])

    if x in cs1516:
        schools15[cs1516[x][0]] = cs1516[x][1]
        if cs1516[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1516[x][0])

    if x in cs1415:
        schools14[cs1415[x][0]] = cs1415[x][1]
        if cs1415[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1415[x][0])


for x in dictclosed2021.keys():

    if x in cs1920:
        schools19[cs1920[x][0]] = cs1920[x][1]
        if cs1920[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1920[x][0])

    if x in cs1819:
        schools18[cs1819[x][0]] = cs1819[x][1]
        if cs1819[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1819[x][0])

    if x in cs1718:
        schools17[cs1718[x][0]] = cs1718[x][1]
        if cs1718[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1718[x][0])

    if x in cs1617:
        schools16[cs1617[x][0]] = cs1617[x][1]
        if cs1617[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1617[x][0])

    if x in cs1516:
        schools15[cs1516[x][0]] = cs1516[x][1]
        if cs1516[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1516[x][0])

    if x in cs1415:
        schools14[cs1415[x][0]] = cs1415[x][1]
        if cs1415[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1415[x][0])


for x in dictclosed2020.keys():

    if x in cs1920:
        schools19[cs1920[x][0]] = cs1920[x][1]
        if cs1920[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1920[x][0])

    if x in cs1819:
        schools18[cs1819[x][0]] = cs1819[x][1]
        if cs1819[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1819[x][0])

    if x in cs1718:
        schools17[cs1718[x][0]] = cs1718[x][1]
        if cs1718[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1718[x][0])

    if x in cs1617:
        schools16[cs1617[x][0]] = cs1617[x][1]
        if cs1617[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1617[x][0])

    if x in cs1516:
        schools15[cs1516[x][0]] = cs1516[x][1]
        if cs1516[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1516[x][0])

    if x in cs1415:
        schools14[cs1415[x][0]] = cs1415[x][1]
        if cs1415[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1415[x][0])


for x in dictclosed2019.keys():

    if x in cs1920:
        schools19[cs1920[x][0]] = cs1920[x][1]
        if cs1920[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1920[x][0])

    if x in cs1819:
        schools18[cs1819[x][0]] = cs1819[x][1]
        if cs1819[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1819[x][0])

    if x in cs1718:
        schools17[cs1718[x][0]] = cs1718[x][1]
        if cs1718[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1718[x][0])

    if x in cs1617:
        schools16[cs1617[x][0]] = cs1617[x][1]
        if cs1617[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1617[x][0])

    if x in cs1516:
        schools15[cs1516[x][0]] = cs1516[x][1]
        if cs1516[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1516[x][0])

    if x in cs1415:
        schools14[cs1415[x][0]] = cs1415[x][1]
        if cs1415[x][0] not in nameOfColleges:
            nameOfColleges.append(cs1415[x][0])
#######################################################################

header = ["School", "2020-2019", "2019-2018",
          "2018-2017", "2017-2016", "2016-2015", "2015-2014"]

# CREATES A LIST OF EACH SCHOOL AND THEIR CORRESPONDING SCORES FOR EACH YEAR
data = []
for x in nameOfColleges:
    recent = [x]
    if x in schools19:
        recent.append(float(schools19[x]))
    else:
        recent.append("NA")

    if x in schools18:
        recent.append(float(schools18[x]))
    else:
        recent.append("NA")

    if x in schools17:
        recent.append(float(schools17[x]))
    else:
        recent.append("NA")

    if x in schools16:
        recent.append(float(schools16[x]))
    else:
        recent.append("NA")

    if x in schools15:
        recent.append(float(schools15[x]))
    else:
        recent.append("NA")
    if x in schools14:
        recent.append(float(schools14[x]))
    else:
        recent.append("NA")
    if "NA" in recent:
        pass
    else:
        data.append(recent)

totalAverage = 0.0
for L in data:
    summ = 0.0
    for x in L[1:]:
        summ += float(x)
    totalAverage += summ/6


# form dataframe from data
df = pd.DataFrame(data, columns=header)

# plot multiple columns such as population and year from dataframe
# df.plot(x="School", y=header[1:],
#        kind="line", figsize=(10, 10))

# display plot
# mp.show()
#######################################################################


# 00345700 for wofford
# 03032500 Alabama State College
x = input("put: ")

schoolscores = []

if x in cs1920:
    schoolscores.append(cs1920[x][1])
else:
    schoolscores.append("NA")
if x in cs1819:
    schoolscores.append(cs1819[x][1])
else:
    schoolscores.append("NA")

if x in cs1718:
    schoolscores.append(cs1718[x][1])
else:
    schoolscores.append("NA")


if x in cs1617:
    schoolscores.append(cs1617[x][1])
else:
    schoolscores.append("NA")


if x in cs1516:
    schoolscores.append(cs1516[x][1])
else:
    schoolscores.append("NA")


if x in cs1415:
    schoolscores.append(cs1415[x][1])
else:
    schoolscores.append("NA")

print(schoolscores)


"""
with open('escuelas.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    writer.writerows(data)
"""
