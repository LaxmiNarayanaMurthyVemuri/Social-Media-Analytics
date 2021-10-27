import pandas as pd
from pandas.io.formats.format import EastAsianTextAdjustment
str="From: Steny Hoyer (Representative from Maryland)"
start=str.find(":")  
end=str.find("(")
Name=str[start+2:end] 
print(Name) 

