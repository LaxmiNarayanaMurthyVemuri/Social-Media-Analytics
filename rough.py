# # def parseName(fromString):
# #     for line in fromString.split("\n"):
# #         print(line)
# #         start = line.find("From") + \
# #          len("From  ")
# #         print(start)
# #         line = line[start:]
# #         end=line.find(" (")
# #         line= line[:end]
    
# #     return line
# # print(parseName("From: Mitch (Senator from Kentucky"))


# def findhastags(message):
#     endChars = [ " ", "\n", "#", ".", ",", "?", "!", ":", ";", ")" ]
#     hastags=[]
#     split_Hastags=message.split("#")
#     for line in split_Hastags[1:len(split_Hastags)]:
#         print(line)
#         startString=""
#         for i in line:
#             if i not in endChars:
#                 startString+=i
#             else:
#                 break
#         finalString="#"+startString
#         hastags.append(finalString)
#     return hastags
# print(findhastags("I am so #excited to watch #TheMandalorian! #starwars"))
# df = makeDataFrame("data/politicaldata.csv")
#     stateDf = makeDataFrame("data/statemappings.csv")
# def addColumns(data, stateDf):
#     names_add=[]
#     positions_add=[]
#     states_add=[]
#     regions_add=[]
#     hashtags_add=[]
#     for index, row in data.iterrows():
#         print(index, row)
#         column_values = data["label"].iloc[index]
#         name=parseName(column_values)
#         position=parsePosition(column_values)
#         state=parseState(column_values)
#         region=getRegionFromState(stateDf,state)
#         text_values= data["text"].iloc[index]
#         hashtags=findHashtags(text_values)
#         names_add.append(name)
#         positions_add.append(position)
#         states_add.append(state)
#         regions_add.append(region)
#         hashtags_add.append(hashtags)
#     data["name"]=names_add
#     data["position"]=positions_add
#     data["state"]=states_add
#     data["region"]=regions_add
#     data["hashtags"]=hashtags_add
#     return
# print(addColumns())