"""
Social Media Analytics Project
Name:
Roll Number:
"""

from typing import Dict
from pandas.core.frame import DataFrame
import hw6_social_tests as test

project = "Social" # don't edit this

### PART 1 ###

import pandas as pd
import nltk
nltk.download('vader_lexicon', quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
endChars = [ " ", "\n", "#", ".", ",", "?", "!", ":", ";", ")" ]

'''
makeDataFrame(filename)
#3 [Check6-1]
Parameters: str
Returns: dataframe
'''
def makeDataFrame(filename):
    df=pd.read_csv(filename)
    return df


'''
parseName(fromString)
#4 [Check6-1]
Parameters: str
Returns: str
'''
def parseName(fromString):
    for i in fromString.split("\n"):
        fromto=i.find(" ")
        str=fromString[fromto:]
        bracket=str.find("(")
        str=str[:bracket]
    return str.strip()


'''
parsePosition(fromString)
#4 [Check6-1]
Parameters: str
Returns: str
'''
def parsePosition(fromString):
    str=""
    for i in fromString.split():
        bracket=(i.find("("))
        if bracket==0:
            str=i.replace("(","")
    return str


'''
parseState(fromString)
#4 [Check6-1]
Parameters: str
Returns: str
'''
def parseState(fromString):
    str=""
    for i in fromString.split("\n"):
        fromto=i.find("from")
        str=fromString[fromto:]
        str=str.replace(")","")
        str=str.replace("from ","")
    return str
    


'''
findHashtags(message)
#5 [Check6-1]
Parameters: str
Returns: list of strs
'''
def findHashtags(message):
    # endChars = [ " ", "\n", "#", ".", ",", "?", "!", ":", ";", ")" ]
    lst=[]
    k="" 
    words=message.split("#") 
    for i in words[1:len(words)]:
        for j in i: 
            if j not in endChars: 
                k+=j 
            else: 
                break 
        k='#'+k 
        lst.append(k) 
        k="" 
    return lst


'''
getRegionFromState(stateDf, state)
#6 [Check6-1]
Parameters: dataframe ; str
Returns: str
'''
def getRegionFromState(stateDf, state):
    df=stateDf.loc[stateDf["state"]==state,"region"]
    return df.values[0]


'''
addColumns(data, stateDf)
#7 [Check6-1]
Parameters: dataframe ; dataframe
Returns: None
'''
def addColumns(data, stateDf):
    name=[]
    position=[]
    state=[]
    region=[]
    hashtags=[]
    for index, row in data.iterrows():
        col_value=data['label'].iloc[index]
        names=parseName(col_value)
        positions=parsePosition(col_value)
        states=parseState(col_value)
        regions=getRegionFromState(stateDf, states)
        txt_value=data['text'].iloc[index]
        hashtag=findHashtags(txt_value)
        name.append(names)
        position.append(positions)
        state.append(states)
        region.append(regions)
        hashtags.append(hashtag)
    data['name']=name
    data['position']=position
    data['state']=state
    data['region']=region
    data['hashtags']=hashtags
    return


### PART 2 ###

'''
findSentiment(classifier, message)
#1 [Check6-2]
Parameters: SentimentIntensityAnalyzer ; str
Returns: str
'''
def findSentiment(classifier, message):
    score = classifier.polarity_scores(message)['compound']
    if score<-0.1:
        return "negative"
    elif score>0.1:
        return "positive"
    else:
        return "neutral"


'''
addSentimentColumn(data)
#2 [Check6-2]
Parameters: dataframe
Returns: None
'''
def addSentimentColumn(data):
    classifier = SentimentIntensityAnalyzer()
    sentiments=[]
    for index, row in data.iterrows():
        txt_value=data["text"].iloc[index]
        result=findSentiment(classifier,txt_value)
        sentiments.append(result)
    data["sentiment"]=sentiments
    return


'''
getDataCountByState(data, colName, dataToCount)
#3 [Check6-2]
Parameters: dataframe ; str ; str
Returns: dict mapping strs to ints
'''
def getDataCountByState(data, colName, dataToCount):
    Dict={}
    if colName!="" and dataToCount!="":
        for index, row in data.iterrows():
            if row[colName]==dataToCount:
                if row["state"] not in Dict:
                    Dict[row["state"]]=0
                Dict[row["state"]]+=1
    else:
        for index, row in data.iterrows():
            if row['state'] not in Dict:
                Dict[row["state"]]=0
            Dict[row["state"]]+=1
    return Dict


'''
getDataForRegion(data, colName)
#4 [Check6-2]
Parameters: dataframe ; str
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def getDataForRegion(data, colName):
    Dict={}
    for index,row in data.iterrows():
        if row["region"] not in Dict:
            Dict[row["region"]]={}
        if row[colName] not in Dict[row["region"]]:
            Dict[row["region"]][row[colName]]=0
        Dict[row["region"]][row[colName]]+=1
    return Dict


'''
getHashtagRates(data)
#5 [Check6-2]
Parameters: dataframe
Returns: dict mapping strs to ints
'''
def getHashtagRates(data):
    Dict={}
    for i in data["hashtags"]:
        for j in i:
            if len(j)!=0 and j not in Dict:
                Dict[j] =1
            else:
                Dict[j]+=1
    return Dict


'''
mostCommonHashtags(hashtags, count)
#6 [Check6-2]
Parameters: dict mapping strs to ints ; int
Returns: dict mapping strs to ints
'''
import operator
def mostCommonHashtags(hashtags, count):
    result={}
    sorted_hastags = dict(sorted(hashtags.items(),key=operator.itemgetter(1),reverse=True))
    for i in range(count):
        for x,y in sorted_hastags.items():
            if len(result)!=count:
                result[x]=y
    return result


'''
getHashtagSentiment(data, hashtag)
#7 [Check6-2]
Parameters: dataframe ; str
Returns: float
'''
def getHashtagSentiment(data, hashtag):
    return


### PART 3 ###

'''
graphStateCounts(stateCounts, title)
#2 [Hw6]
Parameters: dict mapping strs to ints ; str
Returns: None
'''
def graphStateCounts(stateCounts, title):
    import matplotlib.pyplot as plt
    return


'''
graphTopNStates(stateCounts, stateFeatureCounts, n, title)
#3 [Hw6]
Parameters: dict mapping strs to ints ; dict mapping strs to ints ; int ; str
Returns: None
'''
def graphTopNStates(stateCounts, stateFeatureCounts, n, title):
    return


'''
graphRegionComparison(regionDicts, title)
#4 [Hw6]
Parameters: dict mapping strs to (dicts mapping strs to ints) ; str
Returns: None
'''
def graphRegionComparison(regionDicts, title):
    return


'''
graphHashtagSentimentByFrequency(data)
#4 [Hw6]
Parameters: dataframe
Returns: None
'''
def graphHashtagSentimentByFrequency(data):
    return


#### PART 3 PROVIDED CODE ####
"""
Expects 3 lists - one of x labels, one of data labels, and one of data values - and a title.
You can use it to graph any number of datasets side-by-side to compare and contrast.
"""
def sideBySideBarPlots(xLabels, labelList, valueLists, title):
    import matplotlib.pyplot as plt

    w = 0.8 / len(labelList)  # the width of the bars
    xPositions = []
    for dataset in range(len(labelList)):
        xValues = []
        for i in range(len(xLabels)):
            xValues.append(i - 0.4 + w * (dataset + 0.5))
        xPositions.append(xValues)

    for index in range(len(valueLists)):
        plt.bar(xPositions[index], valueLists[index], width=w, label=labelList[index])

    plt.xticks(ticks=list(range(len(xLabels))), labels=xLabels, rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Expects that the y axis will be from -1 to 1. If you want a different y axis, change plt.ylim
"""
def scatterPlot(xValues, yValues, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xValues, yValues)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xValues[i], yValues[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.ylim(-1, 1)

    # a bit of advanced code to draw a line on y=0
    ax.plot([0, 1], [0.5, 0.5], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    # test.week1Tests()
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek1()

    ## Uncomment these for Week 2 ##
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()

    ## Uncomment these for Week 3 ##
    """print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()"""
