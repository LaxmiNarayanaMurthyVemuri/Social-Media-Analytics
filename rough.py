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

