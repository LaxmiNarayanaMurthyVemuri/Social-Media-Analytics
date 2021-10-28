import hw6_social_tests as test
def getDataForRegion(data, colName):
    d={ }
    for index,row in data.iterrows():
        if row["region"] not in d:
            d["region"]={ }
        if row[colName] not in  d["region"]:
                d["region"][row[colName]]=0
        d["region"][row[colName]]+=1
    print(len(d))
    return d 
print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
test.week2Tests()
print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
test.runWeek2()

