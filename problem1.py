# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:36:13 2018

@author: 2356717
"""

import string
message_text = 'defghi'
upper = string.ascii_uppercase
lower = string.ascii_lowercase
shift = 26
#for i in range(len(upper)):
#    if i < len(upper) - shift:
#        print(upper[i+shift], end="")
#    elif i >= len(upper) - shift:
#        j = (i + shift) % len(upper)
#        print(upper[j], end="")

mapping = {}
for i in range(len(upper)):
    if i < len(upper) - shift:
        mapping[upper[i]] = upper[i+shift]
    elif i >= len(upper) - shift:
        j = (i + shift) % len(upper)
        mapping[upper[i]] = upper[j]
for i in range(len(lower)):
    if i < len(lower) - shift:
        mapping[lower[i]] = lower[i+shift]
    elif i >= len(lower) - shift:
        j = (i + shift) % len(lower)
        mapping[lower[i]] = lower[j]
        
#print(mapping)
text = ''
for letter in message_text:
    if letter in mapping:
        text += mapping[letter]
        
print(text)