# -*- coding: utf-8 -*-
"""
Project: Building an Interactive Dictionary
@author: Apoorve Kumar Verma

"""
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w,data.keys())) > 0:
        out = input("Did You mean %s if Yes then press Y else N: " % get_close_matches(w,data.keys())[0] )
        if out == "Y":
            return get_close_matches(w,data.keys())[0]
        elif out == "N":
            return "Match not Found Try again..."
    else:
        return "Not Found"

word = input("Enter Any word: ")
output = translate(word)
if type(output) == list:
    for iteam in output:
        print("=>",iteam)
else:
    print("=>",output)