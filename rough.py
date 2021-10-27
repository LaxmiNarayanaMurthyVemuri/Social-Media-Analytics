# def parseName(fromString):
#     for line in fromString.split("\n"):
#         print(line)
#         start = line.find("From") + \
#          len("From  ")
#         print(start)
#         line = line[start:]
#         end=line.find(" (")
#         line= line[:end]
    
#     return line
# print(parseName("From: Mitch (Senator from Kentucky"))


def parseName(fromString):
    for line in fromString.split("\n"):
        #print(line)
        start = line.find("from ") + \
         len("from ")
        print(start)
        line = line[start:]
        end=line.find(")")
        line=line[:end]
    return line
print(parseName("From: Mitch (Senator from Kentucky)"))